import moviepy.editor as mpe
import cv2
from tkinter import *
from PIL import Image, ImageTk

class Video:
	def __init__(self, counter):
		self.path = "Videos"
		self.fps = 8
		
		self.counter = counter
		photo1 = cv2.imread(f'Photos/IMG_00{counter}1')
		photo2 = cv2.imread(f'Photos/IMG_00{counter}2')
		photo3 = cv2.imread(f'Photos/IMG_00{counter}3')
		photo4 = cv2.imread(f'Photos/IMG_00{counter}4')
		self.photos = [photo1, photo2, photo3, photo4, photo3, photo2]
		self.coords = [(0,0), (0,0), (0,0), (0,0)]
	
	def createVideo(self):
		height, width, layers = self.photos[0].shape
		size = (width, height)
		out = cv2.VideoWriter(f"{self.path}/Video{self.counter}.mp4", cv2.VideoWriter_fourcc(*'mp4v'), self.fps, size)
		
		window = Tk(className="bla")
		img1 = Image.open(f'/home/jamilspi/Code/3DCamera/Photos/IMG_00{self.counter}1')
		img1resize = img1.resize((480, 270))
		image_tk = ImageTk.PhotoImage(img1resize)
		label=Label(window, image=image_tk)
		label.pack()
		
		def click_event(event):
			x, y = event.x, event.y
			print(f"Clicked at ({x}, {y})")
		
		label.bind("<Button-1>", click_event)
		mainloop()
		
		for i in range(self.fps * 5):
			out.write(self.photos[i % 6])
		out.release()
