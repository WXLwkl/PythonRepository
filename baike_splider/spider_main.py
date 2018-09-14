#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Created by xingl on 2018/6/15.
__author__ = 'xingl'

from baike_splider import url_manager, html_downloader, html_outputer, html_parser

class SpiderMain(object):

    def __init__(self):
        self.urls = url_manager.UrlManager()    # url管理器
        self.downloader = html_downloader.HtmlDownloader() # html 下载器
        self.parser = html_parser.HtmlParser()  # html 解析器
        self.outputer = html_outputer.HtmlOutputer()  # html 输出类



    def craw(self, root_url): # 爬虫的调度方法
        print(f"入口url = {root_url}")
        count = 1  # 添加一个变量 查看爬取的是第几个url

        self.urls.add_new_url(root_url)

        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d : %s' % (count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                count += 1
            except:
                print("craw failed!")

        self.outputer.output_html()



if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313?fr=aladdin"
    obj_splider = SpiderMain()
    obj_splider.craw(root_url)
