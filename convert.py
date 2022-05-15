#a simple program to convert image to pdf
# first know location of image

from PIL import Image
image_1 = Image.open(r'location-of-image-and-imagename')
im_1 = image_1.convert('RGB')
im_1.save(r'location to store image and pdf name.')
