#-*-coding:utf-8-*-
import HTMLParser
import urlparse
import urllib
import urllib2
import cookielib
import string
import re

#登录的主页面
hosturl = 'http://192.168.254.220/1.htm'  #登录页面

#post数据接收和处理的页面
posturl = 'http://192.168.254.220/a70.htm'  #处理post请求的url

#设置一个cookie处理器，负责从服务器下载cookie到本地，并在发送请求时带上本地的cookie
cj = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener (cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)

#打开登录主页面（从页面下载cookie，这样我们在发送post数据时就有cookie了，否则发送不成功）
h = urllib2.urlopen (hosturl)

#构造header
header = {
            "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8" ,
            "Accept-Encoding" : "gzip , deflate",
            "Accept-Language" : "zh-CN , zh ; q = 0.8",
            "Cache-Control" : "max-age=0" ,
            "Connection" : "keep-alive" ,
            "Content-Length" : "61" ,
            "Content-Type" : "application/x-www-forn-urlencoded" ,
            "Cookie" :  "md5_login=130891%7C010016",
            "Host" : "192.168.254.220",
            "Origin" : "http://192.168.254.220" ,
            "Referer" : "http://192.168.254.220/a70.htm" ,
            "Upgrade_Insecure_Request" : "1" ,
             "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
            }

user = raw_input ("Please input your userName : ")
password = raw_input ("Please input your password : ")

#构造Post数据
postData = {
                "DDDDD" : user ,
                "upass" : password ,
                "R1" : "0" ,
                "R2" : "",
                "R6" : "0" ,
                "para" : "00" ,
                "0MKKey" : "123456"
            }

#给Post数据编码
postData = urllib.urlencode (postData)

#通过urllib2提供的request方法来向指定Url发送我们构造的数据，并完成登录过程
request = urllib2.Request(posturl , postData , header)
#print request

try : 
    response = urllib2.urlopen (request)
    text = response.read()
    key = text[151:169]
    print (key)
except :
    print "ERROR !!!"

