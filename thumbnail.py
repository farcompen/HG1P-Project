#! /usr/bin/python
# -*- coding:utf-8 -*-

from PIL import Image

size=(128,128)
resim=Image.open("deneme")
resim.thumbnail(size)
resim.save("thumbail","JPEG")
resim.show()