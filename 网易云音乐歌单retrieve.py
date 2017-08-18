import urllib.request,urllib.error,urllib.parse
from bs4 import BeautifulSoup
import re
import json
count=0
http='http://music.163.com/playlist?id='#http://music.163.com/playlist?id=
https='https://music.163.com/playlist?id='

ID=input('Enter your id:')#101152411

url=urllib.request.urlopen(https+ID).read().decode('utf-8')

       
soup=BeautifulSoup(url,'html.parser')

##s=soup.find_all('textarea',limit=1)#href=re.compile('/song?') 这个搜索项不是很强，后期会加入其他搜索条件
s=soup.find('textarea')#find()return a result,unlike find_all return a list
s=s.contents
print(type(s))
s_string=''.join(s) #''.join(s) convert list into string
print(type(s_string))
playlist=json.loads(s_string)

for info in playlist:
    print('Name:',info['name'])
    print('Artist:',info['artists'][0]['name'])
    print('Album:',info['album']['name'])
    print('\n')

##    for l in str(s):
##        l=l.rstrip()
##        if len(l)>0:
##            count=count+1
##print(s)
##    print(count)
##    print(soup)
    ##title=re.findall('b title="(\S+\S)"',url)
    ##title=soup.b
    ##print(title)
    ##for tag in title:
    ##    print(tag)
