# -*- coding:utf-8 -*-

import cv2

if __name__ == "__main__":
    path = "./images/Cubic_Depth_Map.jpg"
    depth = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    # print(image.shape) # [H, W]
    
    # https://docs.opencv.org/3.4/d3/d50/group__imgproc__colormap.html
    # colormap_jet 类似于：红黄橙绿蓝的颜色变化
    depth_color = cv2.applyColorMap(depth, cv2.COLORMAP_JET)
    
    # imshow by OpenCV
    cv2.imshow("depth", depth)
    cv2.imshow("depth_color", depth_color)
    cv2.waitKey(0)
    
    # save result
    #cv2.imwrite(path[0:-4]+"_color.png", depth_color)
