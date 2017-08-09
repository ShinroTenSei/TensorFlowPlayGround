#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 09:39:00 2017

@author: shengtanwu
"""
import os
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    # 读取一帧
    ret, frame = cap.read()
 
    # 转为灰度模式
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 显示帧
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
