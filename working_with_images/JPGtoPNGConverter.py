import sys
import os
from PIL import Image

n = len(sys.argv)
print("Total arguments passed:", n)
# grab first and second argument
path = os.path.join("/Users", "brandon.hernandez", "Documents", "Python Developer Course", "working_with_images")
source = os.path.join(path, sys.argv[1])
dest = os.path.join(path, sys.argv[2])
# check is new / exists, if not create it
if not os.path.isdir(dest):
    os.mkdir(dest)
# loop through Pokedex
for image in os.listdir(source):
    # convert images to png
    jpg_image = Image.open(os.path.join(source, image))
    jpg_image.save(os.path.join(dest, image[:-4]+".png"), "png")
# save to the new folder