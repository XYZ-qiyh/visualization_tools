import os
import cv2
import numpy as np

image_filename = "./color.png"
label_filename = "./sparse_points.jpg"


if __name__ == "__main__":
    image = cv2.imread(image_filename)

    label = cv2.imread(label_filename)

    assert(image.shape == label.shape)

    alpha = 0.25
    beta = (1.0 - alpha)
    blended_image = cv2.addWeighted(image, alpha, label, beta, 0.0)
    cv2.imwrite("blended_image.jpg", blended_image)

    cv2.imshow("blended_image", blended_image)
    cv2.waitKey(0)

