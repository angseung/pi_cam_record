from picamera2 import Picamera2
from time import sleep

picam2 = Picamera2()
# picam2.resolution = (1280, 720)

# picam2.start_preview()
picam2.start(show_preview=True)
sleep(5)
picam2.start_and_capture_file("test_preview.jpg")
# picam2.stop_preview()
