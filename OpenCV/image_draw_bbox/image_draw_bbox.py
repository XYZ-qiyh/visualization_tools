# -*- coding:utf-8 -*-

import os
import cv2
import numpy as np

if __name__ == '__main__':
    image_path = './images/snapshot.png'
    image = cv2.imread(image_path)
    print("image.shape: {}".format(image.shape)) #[H, W, C]

    x, y = 135, 235 # left-top
    w, h = 200, 200  # right-bottom    
    color = (221, 121, 7) #BGR
    thickness = 5
    image_bbox = cv2.rectangle(image, (x, y), (x+w, y+h), color, thickness)
    
    x, y = 250, 620 # left-top
    w, h = 240, 210  # right-bottom    
    image_bbox = cv2.rectangle(image_bbox, (x, y), (x+w, y+h), color, thickness)
    
    winname = 'image_bbox'
    cv2.namedWindow(winname, cv2.WINDOW_KEEPRATIO)
    cv2.imshow(winname, image_bbox)
    cv2.waitKey(0)
    
    output_filename = image_path.replace('.png', '_bbox.png')
    cv2.imwrite(output_filename, image_bbox)

