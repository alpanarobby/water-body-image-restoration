import cv2
import numpy as np
import os

image_path = "C:/Users/alpan/PycharmProjects/impathon/Image296.JPG"

image = cv2.imread(image_path)

image = cv2.resize(image, (512, 512))

x, y = 250, 300
subset = image[y:y+8, x:x+8]

green_channel = image[:, :, 1]

blurred = cv2.blur(image, (15, 15))

restored = cv2.GaussianBlur(blurred, (15, 15), 0)

cv2.imwrite("1_original.png", image)
cv2.imwrite("2_subset_8x8.png", subset)
cv2.imwrite("3_green_channel.png", green_channel)
cv2.imwrite("4_blurred.png", blurred)
cv2.imwrite("5_restored.png", restored)