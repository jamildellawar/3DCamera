import moviepy.editor as mpe
import cv2
from tkinter import *
from PIL import Image, ImageTk
from time import sleep
from anchorGUI import createAnchorGUI

class Video:
	def __init__(self, counter):
		self.pathToExport = "Videos"
		self.fps = 10
		self.pictureAnchors = []
		
		self.counter = counter
		photo1 = cv2.imread(f'Photos/IMG_00{counter}1')
		photo2 = cv2.imread(f'Photos/IMG_00{counter}2')
		photo3 = cv2.imread(f'Photos/IMG_00{counter}3')
		photo4 = cv2.imread(f'Photos/IMG_00{counter}4')
		self.photos = [photo1, photo2, photo3, photo4, photo3, photo2]
		self.coords = [(0,0), (0,0), (0,0), (0,0)]
	
	def getChanges(self, anchors):
		xSum = 0
		ySum = 0
		for anchor in anchors:
			xSum += anchor['x'] * 2
			ySum += anchor['y'] * 2
		xCentroid = round(xSum / 4)
		yCentroid = round(ySum / 4)
		print("xCentroid:" + str(xCentroid))
		print("yCentroid:" + str(yCentroid))
		dx = []
		dy = []
		for anchor in anchors:
			dx.append(xCentroid - anchor['x'] * 2)
			dy.append(yCentroid - anchor['y'] * 2)
			
		return (dx, dy, [xCentroid, yCentroid])	
		
	def calculateCrop(self, dx, dy, centroids):
		print("dx minimum:" + str(min(dx)))
		print("dy minimum:" + str(min(dy)))
		
		box = (max(dx), max(dy), min(min(dx),0) + 1920, min(min(dy),0) + 1080)
		return box
			
		
	def makeFinalEdits(self, photos, dx, dy, centroids, counter):
		cropBox = self.calculateCrop(dx, dy, centroids)
		print(cropBox)
		newHeight = cropBox[2] - cropBox[0]
		newWidth = cropBox[3] - cropBox[1]
		photoPath = f'/home/jamilspi/Code/3DCamera/Photos/IMG_00{str(self.counter)}'
		for i in range(1,5):
			ogImage = Image.open(photoPath + str(i))
			
			newImage = Image.new("RGB", (1920, 1080), (255, 255, 255))
			
			newImage.paste(ogImage, (dx[i-1], dy[i-1]))
			print(dx[i-1])
			print(dy[i-1])
			# newImage.paste(ogImage)
			newImageCropped = newImage.crop(cropBox)
			print("This is the cropBox")
			print(cropBox)
			newImageCropped.save(f'OutputImages/outputImage00{counter}{i}.jpg')
		
		return (newWidth, newHeight)
			
		
			
	def createVideo(self):
		counter = self.counter
		anchors = createAnchorGUI(counter)
		dx, dy, centroids = self.getChanges(anchors)
		
		width, height = self.makeFinalEdits(self.photos, dx, dy, centroids, counter)
		
		size = (height, width)
		print(size)
		# size = (1920, 1080)
		out = cv2.VideoWriter(f"{self.pathToExport}/Video{counter}.mp4", cv2.VideoWriter_fourcc(*'mp4v'), self.fps, size)
		
		photo1 = cv2.imread(f'OutputImages/outputImage00{counter}1.jpg')
		photo2 = cv2.imread(f'OutputImages/outputImage00{counter}2.jpg')
		photo3 = cv2.imread(f'OutputImages/outputImage00{counter}3.jpg')
		photo4 = cv2.imread(f'OutputImages/outputImage00{counter}4.jpg')
		finalPhotos = [photo1, photo2, photo3, photo4, photo3, photo2]
	
		for i in range(self.fps * 5):
			out.write(finalPhotos[i % 6])
		out.release()
