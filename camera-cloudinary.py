import cloudinary
import cloudinary.api
from cloudinary.uploader import uploader
from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
sleep(2)
camera.capture('foo.jpg')
camera.stop_preview()

cloudinary.config(
	cloud_name = 'jartieda',
	api_key = '76545314381111',
	api_secret = '40Vuxz9ENA62Ce29hkxBl7Raaaa'
)

upload('foo.jpg')