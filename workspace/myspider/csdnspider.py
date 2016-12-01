import urllib2
import urllib

#get opinion
url = "https://passport.csdn.net/account/login"
user_agent = "Mozilla/5.0 (X11; Linux x86_64)"
headers = {"User-Agent": user_agent, "Referer": "https://my.csdn.net/my/mycsdn"}
value = {"username": "13667103263", "password": "xccxcc1234567"}
data = urllib.urlencode(value)
request = urllib2.Request(url, data=data, headers=headers)
response = urllib2.urlopen(request)
print response.read()
