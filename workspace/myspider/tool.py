# -*- coding:utf-8 -*-

import os

class Tool:
    
    def __init__(self):
        self.path = '/home/xue/Desktop/QSBKspider'
        if not self.path.endwith('/'):
            self.path = self.path + '/'
        if not os.path.exists(self.path):
            os.mkdir('/home/xue/Desktop/QSBKspider')
            
    def makeDir(self, path):
        path = path.strip()
        dir_path = self.path + path
        exists = os.path.exists(dir_path)
        if not exists:
            os.mkdir(dir_path)
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
        
        
def domain_page(self, response):
    name = response.doc('.mm-p-model-info-left-top dd > a').text()
    brief = response.doc('.mm-aixiu-content').text()
    dir_path = self.Tool.makeDir(name)
    if dir_path:
        img = response.doc('.mm-aixiu-content img').item()
        self.Tool.saveBrief(brief, dir_path, name)
        count = 1
        for img in imgs:
            url = img.attr.src
            if url:
                extension = self.Tool.getExtension(url)
                img_path = dir_path + '/'  + name + str(count) + '.extension' 
                count += 1
                self.crawl(url, call_back =self.save_img)
        
def save_img(self, response):
    img = response.content
    self.Tool.saveImg(img)
           
        
        
                