# -*- coding: utf-8 -*-
"""opencv_face_detect.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14kxHlD5GDCwnkHkvSV2ewKX2Zc6Hipk7

> Upload Image
"""

from google.colab import files
file=files.upload()

"""import libaray"""

import numpy as np
import cv2, os
import matplotlib.pyplot as plt

"""Detecting face and eye using Haar Cascade Classifier"""

face_cascade = cv2.CascadeClassifier('/content/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/content/haarcascade_eye.xml')
img = cv2.imread('/content/hero.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
print(faces)

"""make rectangle"""

for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
plt.grid(None)   
plt.xticks([])
plt.yticks([])
imgplot = plt.imshow(img)

