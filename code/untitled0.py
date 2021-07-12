# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 21:32:53 2021

@author: TuanAnh
"""

"""
Giải tích số - Phương pháp chia đôi
Numerical analysis - Bisection method
"""
import numpy as np
import math 

fx = np.arange(10)
n = 10
def inputF(n):
    for i in range(n + 1):
        print("Nhap vao he so cua x^", n - i)
        temp = input()
        fx[i] = temp
    return fx

def soldF(x0):
    for
print("Nhap vao bac cua ham da thuc")
n = int(input())
inputF(n)