#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  PythonRepository
#  Created by xingl on 2017/11/3.
#  Filename: FileTest


import re

m = re.search('(?<=abcd)ef','abcdef')
print(m.group(0))

