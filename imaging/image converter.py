import os
import sys
from PIL import Image

image_folder = sys.argv[1]
output = sys.argv[2]

if not os.path.exists(output):
    os.makedirs(output)

for files in os.listdir(image_folder):
    img = Image.open(f"{image_folder}\{files}")
    split = files.split(".")[0]
    img.save(f"{output}\{split}.png", "png")
