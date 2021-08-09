from django.utils.text import slugify


PRODUCT_FOLDER = 'products/'


def product_image_handler(instance, filename):
	file_extension = filename.split('.')[-1]
	_filename = f'{PRODUCT_FOLDER}/{slugify(instance.name)}.{file_extension}'

	return _filename
