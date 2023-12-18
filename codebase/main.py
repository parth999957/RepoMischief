import cv2 as cv
import numpy as np
# import os
# import sys


# print(os.getcwd())
image = cv.imread('assets/test_color.png')

# def sample_layer(image):
#     # red = image[:,:,0]

def detect_color(image):
    # Convert the image to HSV color space
    # image = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    # Define the range for the color red
    lower_red = np.array([0, 0, 0])
    upper_red = np.array([200, 200, 255])


    # Create a mask for the color red
    mask = cv.inRange(image, lower_red, upper_red)

   # Display the mask
    # cv.imshow('Mask', mask)
    # cv.waitKey(0)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(image, image, mask=mask)

    return res

# print(image.shape)

newImage = detect_color(image)

cv.imshow('Test Image', newImage)
cv.waitKey(0)

