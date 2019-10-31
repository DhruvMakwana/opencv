from __future__ import print_function
import argparse
from face_detector import FaceDetector
import cv2

# Load the cascade
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", required = True, help = "path to where the face cascade resides")
ap.add_argument("-i", "--image", required = True, help = "path to where the image file resides")
args = vars(ap.parse_args())

face_cascade = cv2.CascadeClassifier(args["face"])

# Read the input image
image = cv2.imread(args["image"])

# Convert into grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

fd = FaceDetector(args["face"])
faceRects = fd.detect(gray, scaleFactor = 1.2, minNeighbors = 5, minSize = (30, 30))
print("I found {} face(s)".format(len(faceRects)))


# Draw rectangle around the faces
for (x, y, w, h) in faceRects:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the output
cv2.imshow('img', image)
cv2.waitKey()