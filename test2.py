#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Created by xingl on 2017/11/16.
__author__ = 'xingl'


import os
x = '/Users/xingl/Desktop/AppIcon/2@2x.png'
fileName = os.path.basename(x)
print(os.path.splitext(fileName)[0])



