from tkinter import *
from PIL import Image, ImageTk

class AnchorGUI(Frame):
	def __init__(self, returnStatement=None, counter=0, master=None):
		pathTo = f'/home/jamilspi/Code/3DCamera/Photos/IMG_00{str(counter)}'
		self.curPicture = 0
		self.picturePaths = [
			pathTo + str(1),
			pathTo + str(2),
			pathTo + str(3),
			pathTo + str(4)
		]
		self.returnStatement = returnStatement
		self.pictureAnchors = []
		
		w, h = 960, 540
		def click_event(event):
			x, y = event.x, event.y
			print(f"Clicked at ({x}, {y})")
			self.pictureAnchors.append((x,y))
			self.returnStatement.set(self.pictureAnchors)
			
			
			self.curPicture += 1
			if self.curPicture < 4:			
				self.nextImage = ImageTk.PhotoImage(Image.open(self.picturePaths[self.curPicture]).resize((w,h)))
				self.label.configure(image=self.nextImage)
				self.label.image=self.nextImage
			else:
				print(self.pictureAnchors)
				master.destroy()
			
		
		Frame.__init__(self, master)
		self.pack()
		
		self.image = ImageTk.PhotoImage(Image.open(self.picturePaths[self.curPicture]).resize((w,h)))
		self.label = Label(image = self.image)
		self.label.bind("<Button-1>", click_event)
		
		self.label.pack()
	
def createAnchorGUI(counter):
	root = Tk()
	returnStatement = StringVar()
	app = AnchorGUI(returnStatement = returnStatement, counter = counter, master = root)
	app.mainloop()
	
	anchors = returnStatement.get().split(",")
	anchor1 = {"x": int(anchors[0][2:]), "y": int(anchors[1][1:-1])}
	anchor2 = {"x": int(anchors[2][2:]), "y": int(anchors[3][1:-1])}
	anchor3 = {"x": int(anchors[4][2:]), "y": int(anchors[5][1:-1])}
	anchor4 = {"x": int(anchors[6][2:]), "y": int(anchors[7][1:-2])}
	print(anchor1)
	print(anchor2)
	print(anchor3) 
	print(anchor4)
	return [anchor1, anchor2, anchor3, anchor4]


createAnchorGUI(10)
