#coding:utf-8
'''
Created on 2016��4��16��

@author: Bai
'''
import urllib
import urllib2
values ={"username":"wbaismile","password":"7333932100"}
data = urllib.urlencode(values)

print "POST方式"
url = "https://passport.csdn.net/account/login?from=http%3A%2F%2Fmy.csdn.net%2Fmy%2Fmycsdn"
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)
print response.read()

print "GET方式"
url2 = "http://passport.csdn.net/account/login"
geturl = url + "?" + data
request2 = urllib2.Request(geturl)
response2 = urllib2.urlopen(request2)
print response2.read()
print geturl


