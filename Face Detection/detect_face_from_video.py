from __future__ import print_function
import argparse
import imutils
from face_detector import FaceDetector
import cv2

# Load the cascade
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", required = True, help = "path to where the face cascade resides")
args = vars(ap.parse_args())

fd = FaceDetector(args["face"])

camera = cv2.VideoCapture(0)


while True:
	(grabbed, frame) = camera.read()

	if not grabbed:
		break

	frame = imutils.resize(frame, width = 300)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faceRects = fd.detect(gray, scaleFactor = 1.1, minNeighbors = 5, minSize = (30,30))
	frameClone = frame.copy()

	for (fX, fY, fW, fH) in faceRects:
		cv2.rectangle(frameClone, (fX, fY), (fX + fW, fY + fH), (0, 255, 0), 2)

	cv2.imshow("Face", frameClone)

	if cv2.waitKey(1) & 0xFF == ord("q"):
		break
camera.release()
cv2.destroyAllWindows()