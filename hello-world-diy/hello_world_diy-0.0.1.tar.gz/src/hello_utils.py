import PIL.Image
import PIL.ImageFilter
import cv2
import functools
import glob
import io
import ipywidgets as widgets
import math
import matplotlib.pyplot as plt
import numpy as np
import os
import tensorflow as tf
import uuid

from ipywebrtc import CameraStream, ImageRecorder, VideoRecorder
# from tensorflow_examples.lite.model_maker.core.task import image_preprocessing
from tflite_model_maker import image_classifier
from tflite_model_maker import model_spec
from tflite_model_maker.image_classifier import DataLoader

GRID_IMG_WIDTH = 120


def set_project_paths(project_name):
    """
    Given a project name creates project dirs for samples and videos

    Parameters
    ----------
        project_name : (str)

    Returns
    -------
        dirs : (str, str)
    """
    project_dir = os.path.abspath(os.path.join(os.pardir, 'projects', project_name))
    project_dir = os.path.normpath(project_dir)

    defective_dir = os.path.join(project_dir, 'images', 'defective')
    os.makedirs(defective_dir, exist_ok=True)

    correct_dir = os.path.join(project_dir, 'images', 'correct')
    os.makedirs(correct_dir, exist_ok=True)

    videos_dir = os.path.join(project_dir, 'videos')
    os.makedirs(videos_dir, exist_ok=True)

    keras_dir = os.path.join(project_dir, 'keras_model')
    os.makedirs(keras_dir, exist_ok=True)

    return project_dir, defective_dir, correct_dir, videos_dir, keras_dir


def collect_samples(dir_name, width=224, height=224):
    """
    Takes snapshots and saves images with shape (320, 240).
    """
    camera = CameraStream(constraints={'audio': False, 'video': {'width': width, 'height': height}})

    out = widgets.Output()

    ok_btn = widgets.Button(
        description='Ok!', icon='check',
        layout=widgets.Layout(width='72px', margin='1 1 1 1'))  # , button_style='success')
    cls_btn = widgets.Button(
        description='Clear', icon='times',
        layout=widgets.Layout(width='72px', margin='1 1 1 1'))  # , button_style='danger')

    image_recorder = ImageRecorder(stream=camera)

    def ok(b, directory=None):
        im = PIL.Image.open(io.BytesIO(image_recorder.image.value))
        rgb_im = im.convert('RGB')
        fn = os.path.join(directory, f'{uuid.uuid4()}.jpg')
        rgb_im.save(fn)
        with out:
            out.clear_output()
            n_images = len(glob.glob(os.path.join(dir_name, '*.jpg')))
            print(f'Images count: {n_images}\nImage saved successfully: {fn}')

    def clear(b):
        with out:
            out.clear_output()

    ok_btn.on_click(functools.partial(ok, directory=dir_name))
    cls_btn.on_click(clear)

    return camera, image_recorder, ok_btn, cls_btn, out


def just_for_fun(image_recorder):
    im = PIL.Image.open(io.BytesIO(image_recorder.image.value))
    return im.filter(PIL.ImageFilter.CONTOUR)


def verify_data(dir_name):
    grid_out = widgets.Output()
    grid_box = widgets.GridBox([], layout=widgets.Layout(grid_template_columns=f'repeat(10, {GRID_IMG_WIDTH + 5}px)'))

    def delete(b, fn=''):
        with grid_out:
            if os.path.exists(fn):
                os.remove(fn)
                grid_out.clear_output()
                print(f'Deleted: {fn}')
                n_images = len(glob.glob(os.path.join(dir_name, '*.jpg')))
                print(f'Images count: {n_images}')
                grid_box.children = create_items()
            else:
                print(f'File has already been deleted: {fn}')

    def create_items():
        fns = glob.glob(os.path.join(dir_name, '*.jpg'))
        fns.sort(key=os.path.getmtime)
        items = []
        for idx, fn in enumerate(fns):
            file = open(fn, 'rb')
            image = file.read()
            im = widgets.Image(value=image, format='jpg', width=GRID_IMG_WIDTH)

            btn = widgets.Button(icon='trash-o', layout=widgets.Layout(width='20px', padding='0 0 0 0', margin='0 0 0 0'))
            btn.add_class('grid-btn-bg')
            btn.on_click(functools.partial(delete, fn=fn))

            vb = widgets.VBox([im, btn])
            vb.layout.align_items = 'center'
            items.append(vb)
        return items

    items = create_items()
    grid_box.children = items

    return grid_box, grid_out


def verify_data_tabs(defective_grid_box, correct_grid_box):
    tab = widgets.Tab()
    tab.children = [defective_grid_box, correct_grid_box]
    tab.set_title(0, 'Defective samples')
    tab.set_title(1, 'Fault-free samples')
    return tab


def plot_image(image, size=(2, 2)):
    plt.figure(figsize=size)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(image)
    plt.show()


def plot_train_images_sample(data):
    plt.figure(figsize=(10, 6))
    for i, (image, label) in enumerate(data.gen_dataset().unbatch().take(15)):
        plt.subplot(3, 5, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(image.numpy(), cmap=plt.cm.gray)
        plt.xlabel(data.index_to_label[label.numpy()])
    plt.show()


def prepare_data(project_dir):
    data = DataLoader.from_folder(os.path.join(project_dir, 'images'))
    train_data, rest_data = data.split(0.8)
    validation_data, test_data = rest_data.split(0.5)
    plot_train_images_sample(train_data)
    return train_data, validation_data, test_data


def get_label_color(val1, val2):
    if val1 == val2:
        return 'green'
    else:
        return 'red'


def plot_predicted_results(model, test_data):
    """
    Plot 30 test images and their color-coded predicted labels
    """
    plt.figure(figsize=(10, 10))
    predicts = model.predict_top_k(test_data)
    for i, (image, label) in enumerate(test_data.gen_dataset().unbatch().take(25)):
        ax = plt.subplot(5, 5, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(image.numpy(), cmap=plt.cm.gray)

        predict_label = predicts[i][0][0]
        color = get_label_color(predict_label, test_data.index_to_label[label.numpy()])
        ax.xaxis.label.set_color(color)
        plt.xlabel('Predicted: %s' % predict_label)
    plt.show()


def create_model(train_data, validation_data):
    model = image_classifier.create(train_data, validation_data=validation_data, batch_size=16)
    print(model.summary())
    return model


def train(train_data, validation_data, n=1):
    for i in range(n):
        model = create_model(train_data, validation_data)
    return model


def setup_video_recorder(project_dir, klass='defective'):
    file_name = os.path.join(project_dir, 'videos', f'{klass}-{uuid.uuid4()}.webm')

    video_recorder_out = widgets.Output()

    camera = CameraStream(constraints={'facing_mode': 'user', 'audio': False, 'video': {'width': 224, 'height': 224}})

    video_recorder = VideoRecorder(stream=camera)

    def save_video(b, file_name):
        video_recorder.save(file_name)
        with video_recorder_out:
            video_recorder_out.clear_output()
            print(f'Successfully saved: {file_name}')

    save_btn = widgets.Button(
        description='Save', icon='download', layout=widgets.Layout(width='72px', margin='1 1 1 1'))
    save_fn = functools.partial(save_video, file_name=file_name)
    save_btn.on_click(save_fn)

    return camera, video_recorder, save_btn, video_recorder_out, file_name


def clear_video_recorder(camera, video_recorder, video_recorder_out):
    camera.close_all()
    video_recorder.close_all()
    video_recorder_out.clear_output()
    video_recorder_out.close_all()


def get_frames_from_video(fn):
    cap = cv2.VideoCapture(fn)
    frames = []
    while True:
        success, frame = cap.read()
        if not success:
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frames.append(frame)
    cap.release()
    return frames


def save_images_as_mp4(frames):
    """Save array of images as an mp4 video"""
    width = frames[0].shape[0]
    height = frames[0].shape[1]
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter('tmp.mp4', fourcc, 25, (width, height))
    for frame in frames:
        writer.write(frame)
    writer.release()


def plot_images(images):
    """Plot images 5 in row with image size approximately 3cm."""
    n_rows = math.ceil(len(images) / 5)
    plt.figure(figsize=(10, n_rows * 2))
    for i, image in enumerate(images):
        plt.subplot(n_rows, 5, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(image, cmap=plt.cm.gray)
    plt.show()


def sample_images(images, rate=5):
    """Sample every nth image."""
    return [images[i] for i in range(0, len(images), 5)]


def save_images(dir_name, frames):
    """Save a set of np array images as jpg."""
    for x in frames:
        fn = os.path.join(dir_name, f'{uuid.uuid4()}.jpg')
        im = PIL.Image.fromarray(x)
        im.save(fn)
    print('Images count:', len(frames))


def detect_blur(fn, threshold=100.):
    """
    Compute the Laplacian of the image and return the focus measure, which is the variance of the Laplacian
    https://pyimagesearch.com/2015/09/07/blur-detection-with-opencv/
    """
    image = cv2.imread(fn)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = cv2.Laplacian(gray_image, cv2.CV_64F).var()
    return fm < threshold


def show_blurry_images(dir_name, threshold=100.):
    p = f'{dir_name}/*.jpg'
    fns = [x for x in glob.glob(p) if detect_blur(x, threshold=threshold)]
    fns.sort(key=os.path.getmtime)
    if len(fns) > 0:
        images = [plt.imread(x) for x in fns]
        plot_images(images)
    else:
        print('No blurry images found.')


def plot_image_w_blur_score(fn, threshold=100.0):
    # https://pyimagesearch.com/2015/09/07/blur-detection-with-opencv/
    image = cv2.imread(fn)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = cv2.Laplacian(gray_image, cv2.CV_64F).var()
    s = 'blurry' if fm < threshold else 'ok'
    cv2.putText(image, f'{s}: {fm:.2f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
    cv2.imshow('test', image)
    cv2.waitKey(0)


def tflite_infer(model_path='projects/fin2/model.tflite'):
    """
    https://www.tensorflow.org/lite/guide/inference
    """
    interpreter = tf.lite.Interpreter(model_path)
    interpreter.allocate_tensors()
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    input_shape = input_details[0]['shape']
    input_data = np.array(np.random.random_sample(input_shape), dtype=np.uint8)

    image = PIL.Image.open('projects/fin2/images/defective/0281af33-17ae-48e7-96e5-2fefac251773.jpg')
    image = image.convert('RGB').resize((224, 224), PIL.Image.ANTIALIAS)

    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    print(output_data)
    return output_data


# def gen_preprocessor(model_name='mobilenet_v2'):
#     """Sample code for generating image preprocessor for a given pre-trained model."""
#     spec = model_spec.get(model_name)
#     preprocessor = image_preprocessing.Preprocessor(
#         spec.input_image_shape, 2, spec.mean_rgb, spec.stddev_rgb, use_augmentation=False)
#     return preprocessor


def predict(model_path='projects/fin2/model.tflite'):
    interpreter = tf.lite.Interpreter(model_path=model_path)
    # or
    # interpreter = tflite.Interpreter(model_content=tflite_model)
    interpreter.resize_tensor_input(0, [1, 224, 224, 3], strict=True)
    interpreter.allocate_tensors()
    interpreter.invoke()


def realtime_evaluate(model, width=224, height=224):
    camera = CameraStream(constraints={'audio': False, 'video': {'width': width, 'height': height}})

    out = widgets.Output()

    predict_btn = widgets.Button(
        description='Predict', icon='microscope',
        layout=widgets.Layout(width='86px', margin='1 1 1 1'))
    cls_btn = widgets.Button(
        description='Clear', icon='times',
        layout=widgets.Layout(width='86px', margin='1 1 1 1'))

    image_recorder = ImageRecorder(stream=camera)

    def predict(b):
        with out:
            im = PIL.Image.open(io.BytesIO(image_recorder.image.value))
            rgb_im = im.convert('RGB')
            im_arr = tf.keras.preprocessing.image.img_to_array(rgb_im)
            tensor, _ = model.preprocess(im_arr, 0, is_training=False)
            tensor = tf.expand_dims(tensor, axis=0)
            pred = model.predict_top_k(tensor, batch_size=1)
            print(f'Prediction: {pred}')

    def clear(b):
        with out:
            out.clear_output()

    predict_btn.on_click(predict)
    cls_btn.on_click(clear)

    return camera, image_recorder, predict_btn, cls_btn, out
