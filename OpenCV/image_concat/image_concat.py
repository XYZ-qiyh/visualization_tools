# -*- coding:utf-8 -*-

import os
import cv2
import numpy as np

if __name__ == '__main__':
    path_image_dir = 'C:\\Users\\ToddyQi\\Desktop\\SceauxCastle\\SceauxCastle\\dense\\0'

    path_image = os.path.join(path_image_dir, 'images\\100_7104.JPG')
    path_depth_map = os.path.join(path_image_dir, 'stereo\\depth_maps\\100_7104_JPG_geometric.png')
    path_normal_map = os.path.join(path_image_dir, 'stereo\\normal_maps\\100_7104_JPG_geometric.png')
    
    image = cv2.imread(path_image)
    print(image.shape) #[H, W, C]
    depth_map = cv2.imread(path_depth_map)
    normal_map = cv2.imread(path_normal_map)
    
    image_concatenated = np.concatenate(
                        (image, depth_map, normal_map), axis=1)
    
    winname = 'image_concatenated'
    cv2.imshow(winname, image_concatenated)
    cv2.waitKey(0)
    
    output_filename = os.path.join(path_image_dir, 'image_concatenated.jpg')
    cv2.imwrite(output_filename, image_concatenated)


