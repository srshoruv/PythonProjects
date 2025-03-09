from PIL import Image, ImageFilter, ImageEnhance

with Image.open("img.jpg") as pic:
    
    rotate = pic.transpose(Image.FLIP_LEFT_RIGHT)
    rotate.save("rotated.jpg")

    bw = pic.convert("L")
    bw.save("BW.jpg")

    blur = pic.filter(ImageFilter.BLUR)
    blur.save("blur.jpg")

    contrast = ImageEnhance.Contrast(pic).enhance(2.5)
    contrast.save("contrast.jpg")

    color = ImageEnhance.Color(pic).enhance(2.5)
    color.save("color.jpg")
    color.show()