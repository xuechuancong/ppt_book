# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import os, string

num = 4
url = 'http://www.qiushibaike.com/8hr/page/' + str(num)
user_agent = 'Mozilla/5.0 (X11; Linux x86_64)'
headers = {'User-Agent': user_agent, 'Referer': 'http://www.qiushibaike.com/'}
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    #print response.read()
    content = response.read()#.decode('utf-8')
    pattern = re.compile('<h2>(.*?)</h2>.*?<div.*?class="content">(.*?)' + 
                                '</div>(.*?)<div class="stats">.*?<span.*?class="stats-vote">.*?<i.*?class="number">(.*?)</i>', re.S)
    items = re.findall(pattern, content)
    x = 0
    pagestor = []
    os.chdir('/home/xue/Desktop/QSBKspider')
    for item in items:
        pagestor.append(item)
        HavImg = re.search('img', item[2])
        if not HavImg:
            x += 1
            #data = {
                    #'name': item[0],
                    #'content': item[1],
                    #'pull': item[3]
                    #}
            print item[0], item[1], item[3]
            File = string.zfill(num, 6) + '.txt'
            f = open(File, 'w') 
            for i in pagestor:
                f.writelines(i)
            f.close()
            #print pagestor
            #print data['name'], data['content']
    print x
    #print pagestor.count([])
        
    
except urllib2.URLError, e:
    if hasattr(e, 'code'):
        print e.code
    if hasattr(e, 'reason'):
        print e.reason
        
    

