import os
import cv2
import numpy as np
from PIL import Image
import glob
import matplotlib.pyplot as plt

def hair_remove(image):
    normalized_image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    grayScale = cv2.cvtColor(normalized_image, cv2.COLOR_RGB2GRAY )
    kernel = cv2.getStructuringElement(1,(9,9)) 
    blackhat = cv2.morphologyEx(grayScale, cv2.MORPH_BLACKHAT, kernel)
    bhg= cv2.GaussianBlur(blackhat,(3,3),cv2.BORDER_DEFAULT)
    ret,mask = cv2.threshold(blackhat,10,255,cv2.THRESH_BINARY)
    dst = cv2.inpaint(normalized_image,mask,6,cv2.INPAINT_TELEA)  
    dst = cv2.resize(dst, (224, 224))
    return dst

current_directory = os.getcwd()

for root, dirs, files in os.walk(current_directory):
    for dir in dirs:
        full_dir_path = os.path.join(root, dir)
        image_files = glob.glob(full_dir_path + '/*.jpg')
        
        for image_file in image_files:
            print(f"Processing image: {image_file}")  # Print the full path of the image
            image = np.asarray(Image.open(image_file).resize((300, 225)))
            processed_img = hair_remove(image)
            processed_img_pil = Image.fromarray(processed_img)
            processed_img_pil.save(image_file)