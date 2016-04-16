#coding:utf-8
'''
Created on 2016��4��16��

@author: Bai
'''
import urllib2
response = urllib2.urlopen("http://www.baidu.com")
#print response.read()
#print response

#构造request
print "Request 方法"
request = urllib2.Request("http://www.baidu.com")
response2 = urllib2.urlopen(request)
print response2.read()