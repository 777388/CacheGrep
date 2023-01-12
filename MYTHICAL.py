import subprocess
from multiprocessing import Process
import sys
import requests
import time
import threading as thread
from proxy_requests.proxy_requests import ProxyRequests
import random
import urllib3
import urllib
import os
from itertools import islice
from multiprocessing import Process
from multiprocessing import Pool
print("usage python3 MYTHICAL.py searchterm domain")
rer = sys.argv[1]
rawr = sys.argv[2]
yup = str(rawr)
wude = open(yup+"output.txt", 'a')
proxx = subprocess.Popen('curl https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt > proxy.txt', stdout=subprocess.PIPE, shell=True).communicate()
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
def toes(titty):
    try:
        while True:
            cookies = {'c_user': '[enter cookie here]', 'xs': '[enter cookie here]'}
            r = requests.get("https://developers.facebook.com/tools/debug/echo/?q=https://translate.google.com/translate?u="+titty, allow_redirects=False, cookies=cookies)
            if r.ok:
                buffnet = open('buffnet.txt', 'w')
                print(r.text, file=buffnet)
                r.raise_for_status()
                buffnet.close()
                buffen = open('buffnet.txt', 'r')
                then = subprocess.Popen("grep -e \"Can\'t reach this website\" buffnet.txt", stdout=subprocess.PIPE, shell=True).communicate()
                if then:
                    print("\rFile "+str(r.url.rstrip())+" not cached", end="")
                    buffen.close()
                    return 5
                else:
                    thun = subprocess.Popen("grep -e "+rer+" buffnet.txt", stdout=subprocess.PIPE, shell=True).communicate()
                    buffen.close()
                    if thun:
                        print(r.url+"")
                        print(r.url, file=wude)
                    else:
                        print("\rdid not find "+rer+" in "+r.url, end="")
                        return 7
            else:
                print("\rtoo many requests sent to facebook or google", end="")
                return 8
    except Exception as e:
        print("\r"+e, end="")

def thongs(litty):
    try:
        while True:
            thong = requests.get("https://cc.bingj.com/cache.aspx?q="+litty.strip(), allow_redirects=False, proxies=proxiess())
            thong.raise_for_status()
            if thong.ok:
                buffer = open('buffer.txt', 'w')
                print(thong.text.strip(), file=buffer)
                buffer.close()
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
                        print("\rdid not find "+rer+" in cache", end='')
                        return 7    
            else:
                print("\rtoo many requests sent to bing, please wait 5 minutes", end='')
                return 8
    except Exception as e:
        print("\r"+e, end="")
        return 9
def taskse(): 
    thing = requests.get("http://web.archive.org/cdx/search/cdx?url="+rawr+"&output=text&fl=original&collapse=urlkey&matchType=prefix")
    if thing.ok:
        stri = "stri.txt"
        fin = open(stri, 'w')
        print(thing.text.strip(), file=fin)
        fil = open(stri, 'r')
    try:
        processes =[Process(target=toes, args=(lineee,)) for lineee in fil]
        processess =[Process(target=thongs, args=(lineee,)) for lineee in fil]
        for process in processes:
            process.start()
        for processs in processess:
            processs.start()
        for process in processes:
            process.join()
        for process in processess:
            process.join()
    except Exception as e:
        print("well, your computer thinks thats too many processes, try a smaller file")
        print(e)
        return e

if __name__ == '__main__':
    taskse()
