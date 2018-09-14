#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Created by xingl on 2018/6/15.
__author__ = 'xingl'

import urllib.request

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        response = urllib.request.urlopen(url)
        if response.getcode() != 200:
            return None
        return  response.read()
