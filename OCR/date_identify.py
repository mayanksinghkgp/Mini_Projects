# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 21:00:53 2021

@author: Mayank 
"""
import cv2
import re
import pytesseract
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
tessdata_dir_config = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"'
img = cv2.imread('invoice.jpg')

d = pytesseract.image_to_data(img, output_type=Output.DICT)
print(d.keys())

date_pattern = '^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)\d\d$'

n_boxes = len(d['text'])
for i in range(n_boxes):
    if float(d['conf'][i]) > 60:
    	if re.match(date_pattern, d['text'][i]):
	        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
	        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imshow('img', img)
cv2.waitKey(0)

im1 = cv2.imread('invoice.jpg')
osd = pytesseract.image_to_osd(im1, config = tessdata_dir_config)
angle = re.search('(?<=Rotate: )\d+', osd).group(0)
script = re.search('(?<=Script: )\d+', osd).group(0)
print("angle: ", angle)
print("script: ", script)