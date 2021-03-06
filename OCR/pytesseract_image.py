# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 16:37:07 2021

@author: Mayank 
"""

import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
import time

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# img = cv2.imread('check1.jpg')
img = cv2.imread('check2.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# cv2.imshow('img',img)
# cv2.waitKey(0)

# hImg, wImg,_ = img.shape
# boxes = pytesseract.image_to_boxes(img)
# for b in boxes.splitlines():
#     print(b)
#     b = b.split(' ')
#     print(b)
#     x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
#     cv2.rectangle(img, (x,hImg- y), (w,hImg- h), (50, 50, 255), 1)
#     cv2.putText(img,b[0],(x,hImg- y-25),cv2.FONT_HERSHEY_SIMPLEX,1,(50,255,50),1)

# cv2.imshow('img', img)
# cv2.waitKey(0)

# hImg, wImg,_ = img.shape
# boxes = pytesseract.image_to_data(img)
# for a,b in enumerate(boxes.splitlines()):
#         print(b)
#         if a!=0:
#             b = b.split()
#             if len(b)==12:
#                 x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
#                 cv2.putText(img,b[11],(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,(50,255,50),2)
#                 cv2.rectangle(img, (x,y), (x+w, y+h), (50, 50, 255), 1)

# cv2.imshow('img', img)
# cv2.waitKey(0)

#### Detecting ONLY Digits  ######
#############################################
hImg, wImg,_ = img.shape
conf = r'--oem 3 --psm 6 outputbase digits'
boxes = pytesseract.image_to_boxes(img,config=conf)
for b in boxes.splitlines():
    print(b)
    b = b.split(' ')
    print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x,hImg- y), (w,hImg- h), (50, 50, 255), 2)
    cv2.putText(img,b[0],(x,hImg- y+25),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)

cv2.imshow('img', img)
cv2.waitKey(0)


