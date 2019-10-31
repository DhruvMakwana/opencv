import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)


resized = imutils.resize(image, width = 100)
cv2.imshow("Resized (width)",resized)
resized = imutils.resize(image, height = 50)
cv2.imshow("Resized (height)",resized)
cv2.waitKey(0)