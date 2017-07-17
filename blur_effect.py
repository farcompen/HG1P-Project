#! /usr/bin/python
# -*- coding:utf-8 -*-

from PIL import Image,ImageFilter


imagee=Image.open("aa")

filtered_image=imagee.filter(ImageFilter.BLUR)
filtered_image.show()
filtered_image.save("filtered.png")

