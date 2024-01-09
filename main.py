from picamera2 import Picamera2, Preview
from libcamera import controls
import time
import os

picam2 = Picamera2(0)
camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")

picam2.configure(camera_config)

picam2.start_preview(Preview.QTGL)
picam2.start()
picam2.set_controls({"AfMode": 1 ,"AfTrigger": 0})
success = picam2.autofocus_cycle()


inputY = True
counter = 0
while inputY:
	if input("press 'y' if you want a picture taken") == 'y':
		picam2.capture_file(f"image{counter}.jpg")
		counter += 1
	else:
		inputY = False
