import os

from PIL import Image, ImageFilter

for files in os.listdir("images"):
    img = Image.open(f"images\{files}")
    split = files.split(".")[0]
    blurred = img.filter(filter=ImageFilter.BLUR)
    blurred.thumbnail((200, 400))
    print(blurred.size)
    blurred.save(f"output\{split}.png", "png")
