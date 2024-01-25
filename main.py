from picamera2 import Picamera2, Preview
from libcamera import controls
import time
import os
from rawImage import Images
from videoMaker import Video

picam2 = Picamera2()
# main={"size": (1920, 1080)},
camera_config = picam2.create_still_configuration(main={"size": (3840, 2160)},lores={"size": (1024, 768)}, display="lores")
print(camera_config)
picam2.configure(camera_config)

picam2.start_preview(Preview.QTGL)
picam2.start()
picam2.set_controls({"AfMode": 0,"AfTrigger": 0, "AfSpeed": 1})
start_time = time.time()
print("Starting Autofocus!")
success = picam2.autofocus_cycle()
print(f"Autofocused: {success}, {time.time() - start_time}")

inputY = True
counter = 0
while inputY:
	userInput = input("press 'y' if you want a picture taken")
	if userInput in {'y', 'timer'}:
		if userInput =='timer':
			time.sleep(3)
		rawPictureDirectory = f"/home/jamilspi/Code/3DCamera/Raw/image{counter}.jpg"
		picam2.capture_file(rawPictureDirectory)
		counter += 1
		time.sleep(1)
		tempImage = Images(rawPictureDirectory)
		time.sleep(1)
		tempImage.separatePictures(counter)
		tempVideo = Video(counter)
		tempVideo.createVideo()
		
		
	elif userInput == "af":
		start_time = time.time()
		print("Fixing Autofocus!")
		success = picam2.autofocus_cycle()
		print(f"Autofocused: {success}, {time.time() - start_time}")
	else:
		inputY = False
