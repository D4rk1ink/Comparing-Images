#!/usr/bin/env python
import numpy as np
import cv2

Pic_A = cv2.imread("pic1a.png")
Pic_B = cv2.imread("pic1b.png")

diff = cv2.absdiff(Pic_A, Pic_B)

cv2.imshow("diff", diff)
cv2.waitKey(0)
