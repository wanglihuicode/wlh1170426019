#定义一个函数，把函数写活
import urllib.request
import urllib.parse
import urllib.get
data = urllib.parse.urlencode({'wd':'太阳'})
print(data)
r=request.get.(url)
r=r.get(url)
url = 'http://www.baidu.com/s?' + data
response = urllib.request.urlopen(url)
HTML = response.read().decode('utf8')
print(HTML)


#把路由和参数写活
import urllib.request
import urllib.parse
import urllib2
import urllib
data={}
data['username']='wp6666666'
data['passworld']='123456'
data = bytes(urllib.parse.urlencode({'pw':'123','un':'456'}),enconding='utf8')
url = 'http://httpbin.org/post'
req=urllib2.urlopen(url,post_data)
content = req.read()
response = urllib.request.urlopen(url,data=data)
result = response.read().decode('utf8')
print(result) 