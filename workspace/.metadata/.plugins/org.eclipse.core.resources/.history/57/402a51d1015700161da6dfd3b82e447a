import urllib2
#import urllib

url = 'http://my.csdn.net/my/mycsdn'
req = urllib2.Request(url)
try:
    urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.code
    print e.reason
    