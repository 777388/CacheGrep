import os
from multiprocessing import Process
import sys
import requests
import time
import urllib3
import threading as thread
urllib3.disable_warnings()
print("usage python3 natotopsecret.py searchterm domain")
rer = sys.argv[1]
rawr = sys.argv[2]
wude = open('outputnts.txt', 'w')
from proxy_requests import proxyrequests

#------------------------------------------------------------

def thumbs(lotty):
    thumb = proxyrequests.get("http://webcache.googleusercontent.com/search?q=cache:"+lotty)
    if thumb.ok:
        buffage = open('buffage.txt', 'w')
        print(thumb.text.strip(), file=buffage)
        buffaged = open('buffage.txt', 'r')
        for lined in buffaged:
            thump = os.popen("grep -e 404 buffaged.txt").read()
            if thump:
                print("saw 404", end='\r')
                continue
            else:
                thenn = os.popen("grep -e "+rer+" buffaged.txt").read()
                if thenn:
                    print("http://webcache.googleusercontent.com/search?q=cache:"+lined, file=wude)
                else:
                    print("did not find "+rer+" in cache", end='\r')
                    continue
    else:
        print("too many requests sent to Google, please wait 5 minutes", end='\r')

def thongs(litty):
    thong = proxyrequests.get("https://cc.bingj.com/cache.aspx?q="+litty)
    if thong.ok:
        buffer = open('buffer.txt', 'w')
        print(thong.text.strip(), file=buffer)
        buffed = open('buffer.txt', 'r')
        for liner in buffed:
            thung = os.popen("grep -e Apologies buffer.txt").read()
            if thung:
                print("saw apologies", end='\r')
                continue
            else:
                theng = os.popen("grep -e "+rer+" buffer.txt").read() 
                if theng:
                    print("https://cc.bingj.com/cache.aspx?q="+liner, file=wude)
                else:
                    print("did not find cache", end='\r')
                    continue
            
    else:
        print("too many requests sent to bing, please wait 5 minutes", end='\r')
        
def taskse():
    for i in range(255):
        for n in range(255):
            for k in range(255):
                for d in range(255):
                    thing = proxyrequests.get("http://web.archive.org/cdx/search/cdx?url="+str(i)+"."+str(n)+"."+str(k)+"."+str(d)+"&output=text&fl=original&collapse=urlkey&matchType=prefix", proxies=proxies)
                    if thing.ok:
                        stri = "stri.txt"
                        fin = open(stri, 'w')
                        print(thing.text.strip(), file=fin)
                        fil = open(stri, 'r')
                        for line in fil:
                            try:
                                thread.Thread(target=thumbs, args=(line,)).start()
                                thread.Thread(target=thongs, args=(line,)).start()
                            except:
                                print("cannot start new thread")
            
                    else:
                        print("too many requests sent to web.archive.org, please wait 5 minutes")
                        time.sleep(300)               
    


if __name__ == '__main__':
    taskse()
