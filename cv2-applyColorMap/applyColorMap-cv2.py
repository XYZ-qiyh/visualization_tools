# -*- coding:utf-8 -*-

import cv2

if __name__ == "__main__":
    path = "./images/Cubic_Depth_Map.jpg"
    depth = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    # print(image.shape) # [H, W]
    
    # https://docs.opencv.org/master/d3/d50/group__imgproc__colormap.html#gadf478a5e5ff49d8aa24e726ea6f65d15
    depth_color = cv2.applyColorMap(depth, cv2.COLORMAP_JET)
    
    # imshow by OpenCV
    cv2.imshow("depth", depth)
    cv2.imshow("depth_color", depth_color)
    cv2.waitKey(0)
    
    # save result
    #cv2.imwrite(path[0:-4]+"_color.png", depth_color)