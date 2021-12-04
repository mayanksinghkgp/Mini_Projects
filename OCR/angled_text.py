# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 23:20:52 2021

@author: Mayank 
"""
import numpy as np
import argparse
import cv2

image = cv2.imread('rotate.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.bitwise_not(gray)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

cv2.imshow('rotated', thresh)
cv2.waitKey(0)


coords = np.column_stack(np.where(thresh > 0))
angle = cv2.minAreaRect(coords)[-1]

if angle < -45:
	angle = -(90 + angle)
else:
	angle = -angle
    
print(angle)
