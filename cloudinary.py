import cloudinary
import cloudinary.api
from cloudinary.uploader import uploader

cloudinary.config(
	cloud_name = 'jartieda',
	api_key = '76545314381111',
	api_secret = '40Vuxz9ENA62Ce29hkxBl7Raaaa'
)

upload('foo.jpg')