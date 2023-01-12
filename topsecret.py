import subprocess
from multiprocessing import Process
import sys
import requests
import time
import threading as thread
from proxy_requests.proxy_requests import ProxyRequests
import random
import urllib3
import os
from multiprocessing import Process
from multiprocessing import Pool
print("usage python3 natotopsecret.py searchterm")
rer = sys.argv[1]

wude = open(rer+'output.txt', 'a')
proxx = subprocess.Popen('curl https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt > proxy.txt', stdout=subprocess.PIPE, shell=True).communicate()

#------------------------------------------------------------
import random
f = open("proxy.txt", "r")
lines = f.readlines()
def random_line(afile):     
    line = random.choice(lines)
    return line.strip()
def proxiess():
    while True:
        ex = str(random_line(f))
        proxies = {
                'http': 'http://'+ex,
            }
        return proxies

def thumbs(lotty):
    try:
        while True: 
            #try:
            r = requests.head("http://webcache.googleusercontent.com/search?q=cache:"+urllib.parse.quote_plus(lotty), allow_redirects=True, proxies=proxiess())
            time.sleep(.1)
            #except requests.exceptions.ProxyError as err:
                #print("Proxy Error", err)
            buffet = open('buffet.txt', 'w')
            print(r.url, file=buffet)
            buffet.close()
            r.raise_for_status()
            buffete = open('buffet.txt', 'r')
            if subprocess.Popen("grep -e sorry buffet.txt", stdout=subprocess.PIPE, shell=True).communicate():
                print("\rredirected to captcha, avoiding", end="")
                #try:
                thumb = requests.get("http://webcache.googleusercontent.com/search?q=cache:"+urllib.parse.quote_plus(lotty), allow_redirects=False, proxies=proxiess())
                time.sleep(.1)
                #except requests.exceptions.ProxyError as err:
                #print("Proxy Error", err)
                if thumb.ok:
                    buffage = open('buffage.txt', 'w')
                    print(thumb.text, file=buffage)
                    thumb.raise_for_status()
                    buffage.close()
                    buffaged = open('buffage.txt', 'r')
                    thump = subprocess.Popen("grep -e 404 buffage.txt", stdout=subprocess.PIPE, shell=True).communicate()
                    if thump:
                        print("\rsaw 404", end='')
                        buffaged.close()
                        return 5
                    else:
                        thenn = subprocess.Popen("grep -e "+rer+" buffage.txt", stdout=subprocess.PIPE, shell=True).communicate()
                        buffaged.close()
                        if thenn:
                            print("http://webcache.googleusercontent.com/search?q=cache:"+urllib.parse.quote_plus(lotty))
                            print("http://webcache.googleusercontent.com/search?q=cache:"+urllib.parse.quote_plus(lotty), file=wude)
                            return 6
                        else:
                            print("\rdid not find "+rer+" in cache", end='')
                            return 7
                else:
                    print("too many requests sent to Google, please wait 5 minutes", end='\r')
                    return 8
            elif subprocess.Popen("grep -e google buffet.txt", stdout=subprocess.PIPE, shell=True).communicate():
                buffete.close()
                #try:
                thumb = requests.get("http://webcache.googleusercontent.com/search?q=cache:"+urllib.parse.quote_plus(lotty), allow_redirects=True, proxies=proxiess())
                thumb.raise_for_status()
                #except requests.exceptions.ProxyError as err:
                    #print("Proxy Error", err)
                if thumb.ok:
                    buffage = open('buffage.txt', 'w')
                    print(thumb.text, file=buffage)
                    thumb.raise_for_status()
                    buffage.close()
                    buffaged = open('buffage.txt', 'r')
                    thump = subprocess.Popen("grep -e 404 buffage.txt", stdout=subprocess.PIPE, shell=True).communicate()
                    if thump:
                        print("\rsaw 404", end='')
                        buffaged.close()
                        return 5
                    else:
                        thenn = subprocess.Popen("grep -e "+rer+" buffage.txt", stdout=subprocess.PIPE, shell=True).communicate()
                        buffaged.close()
                        if thenn:
                            print("http://webcache.googleusercontent.com/search?q=cache:"+urllib.parse.quote_plus(lotty))
                            print("http://webcache.googleusercontent.com/search?q=cache:"+urllib.parse.quote_plus(lotty), file=wude)
                            return 6
                        else:
                            print("\rdid not find "+rer+" in cache", end='')
                            return 7
                else:
                    print("too many requests sent to Google, please wait 5 minutes", end='\r')
                    return 8
            else:
                print("\rredirected to website", end="")
                return 9
    except Exception as e:
        print('\r'+e, end='')
        return 10
def thongs(litty):
    try:
        while True:
            #try:
            thong = requests.get("https://cc.bingj.com/cache.aspx?q="+litty.strip(), allow_redirects=False, proxies=proxiess())
            time.sleep(.1)
            thong.raise_for_status()
            #except requests.exceptions.ProxyError as err: 
                #print("proxy error", err)
            if thong.ok:
                buffer = open('buffer.txt', 'w')
                print(thong.text.strip(), file=buffer)
                buffed = open('buffer.txt', 'r')
                thung = subprocess.Popen("grep -e Apologies buffer.txt", stdout=subprocess.PIPE, shell=True).communicate()
                if thung:
                    print("\rsaw apologies, cache in "+litty.strip()+" not found", end='')
                    return 5
                else:
                    theng = subprocess.Popen("grep -e "+rer+" buffer.txt", stdout=subprocess.PIPE, shell=True).communicate() 
                    if theng:
                        print("https://cc.bingj.com/cache.aspx?q="+litty) 
                        print("https://cc.bingj.com/cache.aspx?q="+litty, file=wude)
                        return 6
                    else:
                        print("\rdid not find cache", end='')
                        return 7    
            else:
                print("\rtoo many requests sent to bing, please wait 5 minutes", end='')
                return 8
    except Exception as e:
        print("\r"+e, end="")
        return 9
def taskse():
    for i in range(255):
        for n in range(255):
            for k in range(255):
                for d in range(255):
                    thing = requests.get("http://web.archive.org/cdx/search/cdx?url="+str(i)+"."+str(n)+"."+str(k)+"."+str(d)+"&output=text&fl=original&collapse=urlkey&matchType=prefix")
                    if thing.ok:
                        stri = "stri.txt"
                        fin = open(stri, 'w')
                        print(thing.text.strip(), file=fin)
                        fil = open(stri, 'r')
                        pool = Pool()
                        try:
                            for lineee in fil:
                                for i in range(len(fil.readlines())):
                                    pool.apply_async(thongs, args=(lineee,))
                                    pool.apply_async(thumbs, args=(lineee,))
                            pool.close()
                            pool.join()
                        except:
                            print("cannot start new thread")
                            return 10
                    else:
                        thing.raise_for_status()
                        print("too many requests sent to web.archive.org, please wait 5 minutes")
                        time.sleep(300)


if __name__ == '__main__':
    taskse()
