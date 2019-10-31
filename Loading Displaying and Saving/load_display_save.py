from __future__ import print_function
import argparse
import cv2

#https://docs.python.org/2/howto/argparse.html
#https://docs.opencv.org/master/db/deb/tutorial_display_image.html
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required = True, 
	help = "Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {} pixels".format(image.shape[2]))

cv2.imshow("Image",image)
cv2.waitKey(3000)