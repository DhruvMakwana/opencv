import cv2

class FaceDetector:
	def __init__(self, faceCascadePath):
		self.faceCascade = cv2.CascadeClassifier(faceCascadePath)

	def detect(self, image, scaleFactor, minNeighbors, minSize):
		rects = self.faceCascade.detectMultiScale(image,
			scaleFactor = scaleFactor,
			minNeighbors = minNeighbors, 
			minSize = minSize,
			flags = cv2.CASCADE_SCALE_IMAGE)
		return rects