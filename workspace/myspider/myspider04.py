import urllib2
import cookielib

cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open("http://my.csdn.net/my/mycsdn")
for items in cookie:
    print 'Name:' + items.name
    print 'Values:' + items.value
    