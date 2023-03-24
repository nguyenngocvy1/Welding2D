from math import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import cv2
from win32api import GetSystemMetrics


# def show(img_name, img):
#     screen_width, screen_height = GetSystemMetrics(0), GetSystemMetrics(1)
#     img_resize = cv2.resize(img,(screen_width,screen_height),interpolation=cv2.INTER_LINEAR)
#     cv2.imshow(img_name,img_resize)

# if __name__ == '__main__':
#     img = cv2.imread('test6.jpg')
#     hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#     # define range of white color in HSV
#     # change it according to your need !
#     lower_white = np.array([0,0,0], dtype=np.uint8)
#     upper_white = np.array([0,0,255], dtype=np.uint8)
    
#     # Threshold the HSV image to get only white colors
#     mask = cv2.inRange(hsv, lower_white, upper_white)
#     # Bitwise-AND mask and original image
#     # res = cv2.bitwise_and(img,img, mask= mask)
#     cv2.imshow('frame',img)
#     cv2.imshow('mask',mask)
#     # cv2.imshow('res',res)
#     cv2.waitKey(0)


l1 = 1 #m for first robotic arm
l2 = 0.5 #m for second robotic arm
x, y = 0,0
q2 = acos((x**2 + y**2 - l1**2 - l2**2)/(2*l1*l2))
q1 = atan(y/x) - atan((l2*sin(q2))/(l1 + l2*cos(q2)))
