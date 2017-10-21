import requests
import random

from bs4 import BeautifulSoup

def qiushibaike():
    content = requests.get('https://www.qiushibaike.com').content
    soup = BeautifulSoup(content,'html.parser')

    for div in soup.find_all('div',{'class':'content'}):
        print div.text.strip()

# import requests
# from bs4 import BeautifulSoup
#
# content = requests.get().cotent
# soup = BeautifulSoup(content,'html.prase')
#
# for div in soup.find_all('div',{'class':'content'}):
#     print div.text.strip()
# import requests
# from bs4 import BeautifulSoup
# content = requests.get().content
# soup = BeautifulSoup(content,'html.prase')
#
# for div in soup.find_all('div',{'class':'content'}):
#     print div.text.strip()
def demo_string():
    stra = 'Hello World!'
    print stra.capitalize()
    strb = '\n\r hello lstrip() \n\n'
    # print strb.lstrip()
    # print strb.rstrip()
    print strb.strip()
    strc = 'llo'
    print 3,strc.startswith('he')
    print 4,strc.endswith('o')
    print 5,stra + strb + strc
    print 6,len(strb)
    print 7,'-'.join(['a','b','c'])
    print 8,stra.split(' ')

def demo_opertion():
    print 4,1<<2
    print 1<2
    print not True
    x = 2
    y = 3.3
    print x,y,type(x),type(y)

def add(a,b):
    return a+b
def sub(a,b):
    return a-b

def demo_dict():
    dicta = {1:1,5:8,3:3}
    print  1,dicta
    print 2,dicta.keys(),dicta.values()
    print 3,dicta.has_key(1),dicta.has_key('3')
    for key,value in dicta.items():
        print 'key-value:',key,value
    ditcb = {'+':add ,'-':sub}
    print 4,ditcb['+'](1,2)
    print 5,ditcb['-'](12,9)

def demo_random():
    print 1,int(random.random() * 100)

if __name__ == '__main__':
    print 'Hello'
   # demo_dict()
    demo_random()
    '''
    print dir(list)
    print chr(90),ord('a')
    '''










