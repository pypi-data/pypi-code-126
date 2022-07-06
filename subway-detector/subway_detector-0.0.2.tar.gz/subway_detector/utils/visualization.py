import os
import cv2


def visualize_results(img,bboxes,output_dir):
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    for bbox in bboxes:
        xmin,ymin,xmax,ymax = bbox[0:4]
        score = round(bbox[4],3)
        cv2.rectangle(img,(int(xmin),int(ymin)),(int(xmax),int(ymax)),(255,0,0),2)
        cv2.putText(img,str(score),(int(xmin),int(ymin - 20)), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    save_path = os.path.join(output_dir,"output.jpg")
    cv2.imwrite(save_path,img)