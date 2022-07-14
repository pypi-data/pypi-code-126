import math
import cv2
import mediapipe as mp
import numpy as np

iris_pts = {
    "left": [470, 471, 472, 469],
    "right": [475, 476, 477, 474],
    "left_center": [468],
    "right_center": [473]
}
eyes_pts = {
    "left": [159, 160, 161, 246, 33, 7, 163, 144, 145, 153, 154, 155, 173, 157, 158],
    "right": [386, 385, 384, 398, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387]
}

lip_pts = {
    "out": [0, 37, 39, 40, 185, 61, 146, 91, 181, 84, 17, 314, 405, 321, 375, 291, 409, 270, 269, 267],
    "lsp_out": [61, 40, 37, 0, 267, 270, 291, 321, 314, 17, 84, 91],
    "lsp_in": [178, 14, 402, 311, 13, 81],
    "in": [13, 82, 81, 80, 191, 78, 95, 88, 178, 87, 14, 317, 402, 318, 324, 308, 415, 310, 311, 312],
    "in_rect": [13, 14, 61, 291]  # 上下左右
    # "in_rect": [13, 14, 95, 415]  # 上下左右
}

eyebrow_pts = {
    "left": [105, 63, 70, 46, 53, 52, 65, 55, 107, 66],
    "right": [334, 296, 336, 285, 295, 282, 283, 276, 300, 293]
}

nose_pts = {
    "out": [197, 3, 236, 198, 209, 49, 129, 64, 98, 240, 75, 60, 99, 97, 2, 326, 328, 290, 305, 460, 327, 294, 358, 279,
            429, 420, 456, 248],
    "center": [4]
}
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=True,
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5)

mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(
    model_selection=1, min_detection_confidence=0.5)


# 获取两个点的欧式距离
def get_points_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# 人脸检测
def get_face_box(cv2_img):
    results = face_detection.process(cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB))
    # Draw face detections of each face.
    if not results.detections:
        return None
    return results.detections[0]


# 检测人脸
def get_detect_face(cv2_img, detection):
    annotated_image = cv2_img.copy()
    mp_drawing.draw_detection(annotated_image, detection)
    return annotated_image


# 获取roi图片
def get_roi_image(cv2_img, roi_box):
    x1, y1, x2, y2 = roi_box
    return cv2_img.copy()[y1:y2, x1:x2]


# 获取gj mask roi人脸区域
def get_face_roi_box(cv2_img, detect_box, zoom_ratio, top_ratio):
    cv2_img_height, cv2_img_width = cv2_img.shape[:2]
    x1 = detect_box.xmin
    y1 = detect_box.ymin
    box_width = detect_box.width
    box_height = detect_box.height
    x2 = x1 + box_width
    y1 = y1 - box_height * top_ratio
    x1 = int((x1 - box_width * zoom_ratio) * cv2_img_width)
    x2 = int((x2 + box_width * zoom_ratio) * cv2_img_width)
    y1 = int(y1 * cv2_img_height)
    y2 = y1 + (x2 - x1)
    return [x1, y1, x2, y2]


# 获取按次序的人脸轮廓数组下标list
def _get_sorted_contours_idx(_contours_idx):
    _sorted_contours_idx = []
    count = 1
    max_warning_threshold = 1000
    for _iter in _contours_idx:
        start = _iter[0]
        break
    _sorted_contours_idx.append(start)
    while True:
        max_warning_threshold -= 1
        for item in _contours_idx:
            if item[0] == start:
                _sorted_contours_idx.append(item[1])
                start = item[1]
                count += 1
                break
        if count >= len(_contours_idx):
            break
        if max_warning_threshold <= 0:
            print("[ERROR]:未发现一个闭合的边界点idx,请检查输入的_contours_idx参数")
            return []
    return _sorted_contours_idx


contours_idx = _get_sorted_contours_idx(mp_face_mesh.FACEMESH_FACE_OVAL)


# 获取特定点坐标
def get_specific_points(cv2_img, face_landmark, points_idx):
    height, width = cv2_img.shape[:2]
    points = []
    for idx in points_idx:
        x = int(face_landmark.landmark[idx].x * width)
        y = int(face_landmark.landmark[idx].y * height)
        points.append((x, y))
    return points


# 获取瞳孔坐标
def get_iris_center_points(cv2_img, face_landmark=None):
    if not face_landmark:
        face_landmark = get_landmark(cv2_img)
    return get_specific_points(cv2_img, face_landmark, iris_pts["left_center"] + iris_pts["right_center"])


# 获取鼻尖坐标
def get_nose_center_points(cv2_img, face_landmark=None):
    if not face_landmark:
        face_landmark = get_landmark(cv2_img)
    return get_specific_points(cv2_img, face_landmark, nose_pts["center"])


# 获取嘴巴中心坐标&角度
def get_lip_center_points_with_degree(cv2_img, face_landmark=None):
    if isinstance(face_landmark, type(None)):
        face_landmark = get_landmark(cv2_img)
    [x1, y1], [x2, y2] = get_specific_points(cv2_img, face_landmark, [61, 291])
    [x3, y3], [x4, y4] = get_specific_points(cv2_img, face_landmark, [13, 14])
    theta = math.atan((y2 - y1) / (x2 - x1))
    x_c = (x1 + x2) // 2
    y_c = (y3 + y4) // 2
    return x3, y3, theta  # x_c, y_c, theta


# 获取嘴巴内嘴唇的宽度&高度
def get_in_lip_shape(cv2_img, face_landmark=None):
    if isinstance(face_landmark, type(None)):
        face_landmark = get_landmark(cv2_img)
    (tp_x, tp_y), (bp_x, bp_y), (lp_x, lp_y), (rp_x, rp_y) = get_specific_points(cv2_img, face_landmark,
                                                                                 lip_pts["in_rect"])
    lip_width = int(get_points_distance(lp_x, lp_y, rp_x, rp_y))
    lip_height = int(get_points_distance(tp_x, tp_y, bp_x, bp_y))
    theta = math.atan((rp_y - lp_y) / (rp_x - lp_x))
    return lip_width, lip_height, theta


# 获取landmark
def get_landmark(cv2_img):
    results = face_mesh.process(cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB))
    # Print and draw face mesh landmarks on the image.
    if not results.multi_face_landmarks:
        return None
    return results.multi_face_landmarks[0]


# 获取人脸mask
def get_mask(cv2_img, face_landmarks):
    height, width = cv2_img.shape[:2]
    black_img = np.zeros_like(cv2_img)
    contours_value = []
    for idx in contours_idx:
        x = int(face_landmarks.landmark[idx].x * width)
        y = int(face_landmarks.landmark[idx].y * height)
        contours_value.append([x, y])
    cv2.fillPoly(black_img, np.array([[contours_value]]), (255, 255, 255))
    return cv2.cvtColor(black_img, cv2.COLOR_BGR2GRAY)


# 获取人脸五官mask
def get_seg_facial_features(cv2_img, face_landmarks, need_features=["eye", "eyebrow", "lip", "nose", "lsp_lip"],
                            color_list=[(255, 255, 255)], need_contour_line=True):
    # need_features support => ["eye", "eyebrow", "iris","lip","nose"]
    height, width = cv2_img.shape[:2]
    if len(color_list) < len(need_features):
        for i in range(0, len(need_features) - len(color_list)):
            color_list.append(color_list[-1])
    color_id = 0
    black_img = np.zeros_like(cv2_img)
    if "eye" in need_features:
        contours_idx = [eyes_pts["left"], eyes_pts["right"]]
        for contour_idx in contours_idx:
            contour_value = []
            for idx in contour_idx:
                x = int(face_landmarks.landmark[idx].x * width)
                y = int(face_landmarks.landmark[idx].y * height)
                contour_value.append([x, y])
            cv2.fillPoly(black_img, np.array([[contour_value]]), color_list[color_id])
        color_id += 1
    if "eyebrow" in need_features:
        contours_idx = [eyebrow_pts["left"], eyebrow_pts["right"]]
        for contour_idx in contours_idx:
            contour_value = []
            for idx in contour_idx:
                x = int(face_landmarks.landmark[idx].x * width)
                y = int(face_landmarks.landmark[idx].y * height)
                contour_value.append([x, y])
            cv2.fillPoly(black_img, np.array([[contour_value]]), color_list[color_id])
        color_id += 1
    if "iris" in need_features:
        contours_idx = [iris_pts["left"], iris_pts["right"]]
        for contour_idx in contours_idx:
            contour_value = []
            for idx in contour_idx:
                x = int(face_landmarks.landmark[idx].x * width)
                y = int(face_landmarks.landmark[idx].y * height)
                contour_value.append([x, y])
            cv2.fillPoly(black_img, np.array([[contour_value]]), color_list[color_id])
        color_id += 1
    if "nose" in need_features:
        contours_idx = [nose_pts["out"]]
        for contour_idx in contours_idx:
            contour_value = []
            for idx in contour_idx:
                x = int(face_landmarks.landmark[idx].x * width)
                y = int(face_landmarks.landmark[idx].y * height)
                contour_value.append([x, y])
            cv2.fillPoly(black_img, np.array([[contour_value]]), color_list[color_id])
        color_id += 1
    if "lip" in need_features:
        contour_value = []
        for idx in lip_pts["out"]:
            x = int(face_landmarks.landmark[idx].x * width)
            y = int(face_landmarks.landmark[idx].y * height)
            contour_value.append([x, y])
        cv2.fillPoly(black_img, np.array([[contour_value]]), color_list[color_id])
        contour_value = []
        for idx in lip_pts["in"]:
            x = int(face_landmarks.landmark[idx].x * width)
            y = int(face_landmarks.landmark[idx].y * height)
            contour_value.append([x, y])
        cv2.fillPoly(black_img, np.array([[contour_value]]), (0, 0, 0))
    if "lsp_lip" in need_features:
        contour_value = []
        for idx in lip_pts["lsp_out"]:
            x = int(face_landmarks.landmark[idx].x * width)
            y = int(face_landmarks.landmark[idx].y * height)
            contour_value.append([x, y])
        cv2.fillPoly(black_img, np.array([[contour_value]]), color_list[color_id])
        contour_value = []
        for idx in lip_pts["lsp_in"]:
            x = int(face_landmarks.landmark[idx].x * width)
            y = int(face_landmarks.landmark[idx].y * height)
            contour_value.append([x, y])
        cv2.fillPoly(black_img, np.array([[contour_value]]), (0, 0, 0))
    if need_contour_line:
        mp_drawing.draw_landmarks(
            image=black_img,
            landmark_list=face_landmarks,
            connections=mp_face_mesh.FACEMESH_FACE_OVAL,
            landmark_drawing_spec=None,
            connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_contours_style())
    return black_img
