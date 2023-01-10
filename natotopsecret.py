import os
from multiprocessing import Process
import sys
import requests
import time
import threading as thread
print("usage python3 natotopsecret.py searchterm domain")
rer = sys.argv[1]
rawr = sys.argv[2]
wude = open('outputnts.txt', 'a')

#------------------------------------------------------------

def thumbs(lotty):
    while True: 
        r = requests.head("http://webcache.googleusercontent.com/search?q=cache:"+lotty, allow_redirects=True)
        buffet = open('buffet.txt', 'w')
        print(r.url, buffet)
        buffete = open('buffet.txt', 'r')
        if os.popen("grep -e sorry buffet.txt").read():
            print("redirected to captcha, avoiding", end="\r")
            thumb = requests.get("http://webcache.googleusercontent.com/search?q=cache:"+lotty, allow_redirects=False)
            if thumb.ok:
                buffage = open('buffage.txt', 'w')
                print(thumb.text.strip(), file=buffage)
                buffaged = open('buffage.txt', 'r')
                for lined in buffaged:
                    thump = os.popen("grep -e 404 buffage.txt").read()
                    if thump:
                        print("saw 404", end='\r')
                        return 5
                    else:
                        thenn = os.popen("grep -e "+rer+" buffage.txt").read()
                        if thenn:
                            print("http://webcache.googleusercontent.com/search?q=cache:"+lined, file=wude)
                            return 6
                        else:
                            print("did not find "+rer+" in cache", end='\r')
                            return 7
            else:
                print("too many requests sent to Google, please wait 5 minutes", end='\r')
                return 8
        elif os.popen("grep -e google buffet.txt").read():
            thumb = requests.get("http://webcache.googleusercontent.com/search?q=cache:"+lotty, allow_redirects=True)
            if thumb.ok:
                buffage = open('buffage.txt', 'w')
                print(thumb.text.strip(), file=buffage)
                buffaged = open('buffage.txt', 'r')
                for lined in buffaged:
                    thump = os.popen("grep -e 404 buffage.txt").read()
                    if thump:
                        print("saw 404", end='\r')
                        return 5
                    else:
                        thenn = os.popen("grep -e "+rer+" buffage.txt").read()
                        if thenn:
                            print("http://webcache.googleusercontent.com/search?q=cache:"+lined, file=wude)
                            return 6
                        else:
                            print("did not find "+rer+" in cache", end='\r')
                            return 7
            else:
                print("too many requests sent to Google, please wait 5 minutes", end='\r')
                return 8
        else:
            print("redirected to website", end="\r")
            return 9
def thongs(litty):
    while True:
        thong = requests.get("https://cc.bingj.com/cache.aspx?q="+litty, allow_redirects=False)
        if thong.ok:
            buffer = open('buffer.txt', 'w')
            print(thong.text.strip(), file=buffer)
            buffed = open('buffer.txt', 'r')
            for liner in buffed:
                thung = os.popen("grep -e Apologies buffer.txt").read()
                if thung:
                    print("saw apologies", end='\r')
                    return 5
                else:
                    theng = os.popen("grep -e "+rer+" buffer.txt").read() 
                    if theng:
                        print("https://cc.bingj.com/cache.aspx?q="+liner, file=wude)
                        return 6
                    else:
                        print("did not find cache", end='\r')
                        return 7    
        else:
            print("too many requests sent to bing, please wait 5 minutes", end='\r')
            return 8
def taskse():
    thing = requests.get("http://web.archive.org/cdx/search/cdx?url="+rawr+"&output=text&fl=original&collapse=urlkey&matchType=prefix")
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
