# Converting an image from colour to grayscale using OpenCV
# Ref: https://www.tutorialspoint.com/converting-an-image-from-colour-to-grayscale-using-opencv
# Date: 2022-01-10

import os
import cv2

if __name__ == "__main__":
    image_path = "lena.jpg"
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    out_image_path = image_path.replace(".jpg", "_gray.jpg")
    cv2.imwrite(out_image_path, gray)
