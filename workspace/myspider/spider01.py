#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2016-08-22 16:51:34
# Project: taobaogirl


from pyspider.libs.base_handler import *
import os

class Handler(BaseHandler):
    crawl_config = {
    }
    
    def __init__(self):
        self.baseurl = 'https://mm.taobao.com/json/request_top_list.htm?page='
        self.startpage = 1
        self.endpage = 30
        self.tool = Tool()
        
    @every(minutes=24 * 60)
    def on_start(self):
        while self.startpage <= self.endpage:
            url = self.baseurl + str(self.startpage)
            print url
            self.crawl(url, callback=self.index_page)
            self.startpage += 1
            
    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('.lady-name').items():
            self.crawl(each.attr.href, callback=self.detail_page, fetch_type='js')

    @config(priority=2)
    def detail_page(self, response):
        domain = response.doc('.mm-p-domain-info li > span').text()
        if domain:
            page_url = 'https:' + domain
            self.crawl(page_url, callback=self.domain_page)
        
    def domain_page(self, response):
        name = response.doc('.mm-p-model-info-left-top dd > a').text()
        brief = response.doc('.mm-aixiu-content').text()
        dir_path = self.tool.makeDir(name)
        if dir_path:
            imgs = response.doc('.mm-aixiu-content img').items()
            self.tool.saveBrief(brief, dir_path, name)
            count = 1
            for img in imgs:
                url = img.attr.src
                if url:
                    extension = self.tool.getExtension(url)
                    img_path = dir_path + '/'  + name + str(count) + '.extension' 
                    count += 1
                    self.crawl(url, call_back =self.save_img,
                                save={'img_path': img_path})
          
    def save_img(self, response):
        img = response.content
        img_path = response.save['img_path']
        self.Tool.saveImg(img, img_path)
    
    

class Tool:
    
    def __init__(self):
        self.path = '/home/xue/Desktop/QSBKspider'
        if not self.path.endswith('/'):
            self.path = self.path + '/'
        if not os.path.exists(self.path):
            os.mkdir('/home/xue/Desktop/QSBKspider/')
            
    def makeDir(self, path):
        path = path.strip()
        dir_path = self.path + path
        exists = os.path.exists(dir_path)
        if not exists:
            os.mkdirs(dir_path)
            return dir_path
        else:
            return dir_path
        
    def saveImg(self, content, img_path):
        f = open(img_path, 'wb')
        f.write(content)
        f.close()
        
    def saveBrief(self, content, dir_path, name):
        file_name = dir_path + '/' + name + '.txt'
        f = open(file_name, 'w+')
        f.write(content.encode('utf-8'))
        f.close()
        
    def getExtension(self, url):
        Extension = url.split('.')[-1]
        return Extension
    
    
    
    
    
    
    