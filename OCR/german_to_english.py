# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 17:48:54 2021

@author: Mayank 
"""

from textblob import TextBlob
import pytesseract
import cv2



image = cv2.imread('check_german.jpg')
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# OCR the image, supplying the country code as the language parameter
options = "-l {} --psm {}".format('deu', 13)
text = pytesseract.image_to_string(rgb, config=options)
# show the original OCR'd text
print("ORIGINAL")
print("========")
print(text)
print("")

tb = TextBlob(text)
translated = tb.translate(to='eng')
# show the translated text
print("TRANSLATED")
print("==========")
print(translated)



