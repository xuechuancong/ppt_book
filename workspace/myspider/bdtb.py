#print 'd'
# -*- coding:utf-8 -*-
import re, os
import urllib2
import urllib

class BDTB:
    
    def __init__(self, baseURL, seeLZ):
        self.baseURL = baseURL
        self.seeLZ = '?seeLZ=' + str(seeLZ)
        
    def getpage(self, pn):
        self.pn = pn
        try:
            url = self.baseURL + self.seeLZ + '&pn=' + str(pn)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            #print response.read()
            return response.read()  
        except urllib2.URLError, e:
            #print e.reason()
            return e.reason
 
    def getTitle(self):
        page = self.getpage(1)
        pattern = re.compile('<h3 class="core_title_txt pull-left text-overflow.*?>(.*?)</h3>', re.S)
        result = re.search(pattern, page)
        if result:
            #print result.group(1).strip()
            return result.group(1).strip()
        else:
            return None
 
    def getcontent(self):
        page = self.getpage(1)
        pattern = re.compile('<div.*?class="d_post_content j_d_post_content ">(.*?)</div>', re.S)
        items = re.findall(pattern, page)
        content = []
        os.chdir('/home/xue/Desktop/QSBKspider')
        f = open('bdtb.txt', 'w')
        for item in items:
            content.append(item)
        for i in content:
            print i
            f.writelines(i)
        f.close()
        
baseURL = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseURL, 1)
bdtb.getTitle()
bdtb.getcontent() 

    

            
            
            
            
            
            

            
                    

    
