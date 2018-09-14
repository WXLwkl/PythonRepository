#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Created by xingl on 2018/6/20.
__author__ = 'xingl'


from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        root = Tk()
        root.resizable(width=False, height=False)
        Label(root, text=u'姓名:').grid(row=0, column=0, sticky=W, padx=3, pady=3)
        ename = Entry(root, width=8)
        ename.grid(row=0, column=1, sticky=W, padx=3, pady=3)
        Label(root, text=u'性别:').grid(row=0, column=2, sticky=W, padx=3, pady=3)
        esex = Entry(root, width=8)
        esex.grid(row=0, column=3, sticky=W, padx=3, pady=3)
        Label(root, text=u'民族:').grid(row=0, column=4, sticky=W, padx=3, pady=3)
        enation = Entry(root, width=8)
        enation.grid(row=0, column=5, sticky=W, padx=3, pady=3)
        Label(root, text=u'出生年:').grid(row=1, column=0, sticky=W, padx=3, pady=3)
        eyear = Entry(root, width=8)
        eyear.grid(row=1, column=1, sticky=W, padx=3, pady=3)
        Label(root, text=u'月:').grid(row=1, column=2, sticky=W, padx=3, pady=3)
        emon = Entry(root, width=8)
        emon.grid(row=1, column=3, sticky=W, padx=3, pady=3)
        Label(root, text=u'日:').grid(row=1, column=4, sticky=W, padx=3, pady=3)
        eday = Entry(root, width=8)
        eday.grid(row=1, column=5, sticky=W, padx=3, pady=3)
        Label(root, text=u'住址:').grid(row=2, column=0, sticky=W, padx=3, pady=3)
        eaddr = Entry(root, width=32)
        eaddr.grid(row=2, column=1, sticky=W, padx=3, pady=3, columnspan=5)
        Label(root, text=u'证件号码:').grid(row=3, column=0, sticky=W, padx=3, pady=3)
        eidn = Entry(root, width=32)
        eidn.grid(row=3, column=1, sticky=W, padx=3, pady=3, columnspan=5)
        Label(root, text=u'签发机关:').grid(row=4, column=0, sticky=W, padx=3, pady=3)
        eorg = Entry(root, width=32)
        eorg.grid(row=4, column=1, sticky=W, padx=3, pady=3, columnspan=5)
        Label(root, text=u'有效期限:').grid(row=5, column=0, sticky=W, padx=3, pady=3)
        elife = Entry(root, width=32)
        elife.grid(row=5, column=1, sticky=W, padx=3, pady=3, columnspan=5)
        Label(root, text=u'选项:').grid(row=6, column=0, sticky=W, padx=3, pady=3)
        ebgvar = IntVar()
        ebg = Checkbutton(root, text=u'自动抠图', variable=ebgvar)
        ebg.grid(row=6, column=1, sticky=W, padx=3, pady=3, columnspan=5)
        Button(root, text=u'生成', width=32, command=generator).grid(row=7, column=1, sticky=W, padx=3, pady=3, columnspan=4)


app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()


# '''
# 50行Python爬取猫眼电影TOP100榜单信息
# '''
#
# import requests, re, json
# from multiprocessing import Pool
#
#
# from requests.exceptions import RequestException
#
# headers = {'User-Agent':'Mozilla/5.0 '}
#
# def get_one_page(url):
#     try:
#         res = requests.get(url, headers=headers)
#         if res.status_code == 200:
#             return res.text
#         return None
#     except RequestException:
#         return None
#
# def parse_one_page(html):
#
#     pattern = re.compile('.*?board-index.*?>(\d+).*?src="(.*?)".*?name">'
#
#                          + '.*?>(.*?).*?star">(.*?).*?releasetime">(.*?)'
#
#                          + '.*?integer">(.*?).*?fraction">(.*?).*?', re.S)
#
#     items = re.findall(pattern, html)
#     for item in items:
#         yield {
#             'index': item[0],
#             'image': item[1],
#             'title': item[2],
#             'actor': item[3].strip()[3:],
#             'time': item[4].strip()[5:],
#             'score': item[5] + item[6]
#         }
#
#
# def write_to_file(content):
#     with open('result.txt', 'a', encoding='utf-8') as f:
#         f.write(json.dumps(content, ensure_ascii=False) + '\n')
#
#
# def main(offset):
#     url = 'http://maoyan.com/board/4?offset=' + str(offset)
#     # print("url=", url)
#     html = get_one_page(url)
#
#     for item in parse_one_page(html):
#         print(item)
#         write_to_file(item)
#
#
# if __name__ == '__main__':
#
#     p = Pool()
#     p.map(main, [i * 10 for i in range(10)])