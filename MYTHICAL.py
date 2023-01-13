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
from requests.utils import unquote
import os
from itertools import islice
from multiprocessing import Process
from multiprocessing import Pool
print("usage python3 MYTHICAL.py searchterm domain")
rer = sys.argv[1]
rawr = sys.argv[2]
yup = str(rawr)
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
    wude = open(yup+"output.txt", 'a')
    try:
        while True:
            cookies = {'c_user': '[cookie]', 'xs': '[cookie]'}
            r = requests.get("https://developers.facebook.com/tools/debug/echo/?q=https://translate.google.com/translate?u="+unquote(titty.strip()), proxies=proxiess(), allow_redirects=True, cookies=cookies)
            if r.ok:
                buffnet = open('buffnet.txt', 'w')
                print(r.text, file=buffnet)
                r.raise_for_status()
                buffnet.close()
                buffen = open('buffnet.txt', 'r')
                then = subprocess.Popen("grep reach buffnet.txt", stdout=subprocess.PIPE,  stderr = subprocess.PIPE, shell=True)
                thenn = subprocess.Popen("grep 'error occured' buffnet.txt", stdout=subprocess.PIPE,  stderr = subprocess.PIPE, shell=True)
                if then.stdout.readline().decode('utf-8'):
                    print(then)
                    print("\rFile "+str(r.url.rstrip())+" not cached", end="")
                    buffen.close()
                    return 5
                elif thenn.stdout.readline().decode('utf-8'): 
                    print("\rError on facebook", end="")
                    return 6
                    
                else:
                    thun = subprocess.Popen("grep -e "+rer+" buffnet.txt", stdout=subprocess.PIPE, stderr = subprocess.PIPE, shell=True)
                    buffen.close()
                    if thun.stdout.readline().decode('utf-8'):
                        print(r.url+"")
                        print(r.url, file=wude)
                        wude.close()
                        return 4
                    else:
                        print("\rdid not find "+rer+" in "+r.url, end="")
                        return 7
            else:
                print(r.url)
                print("\rtoo many requests sent to facebook or google", end="")
                return 8
    except Exception as e:
        print("\r"+e, end="")

def thongs(litty):
    wude = open(yup+"output.txt", 'a')
    try:
        while True:
            thong = requests.get("https://cc.bingj.com/cache.aspx?q="+litty.strip(), allow_redirects=False, proxies=proxiess())
            thong.raise_for_status()
            if thong.ok:
                buffer = open('buffer.txt', 'w')
                print(thong.text.strip(), file=buffer)
                buffer.close()
                thung = subprocess.Popen("grep -e Apologies buffer.txt", stdout=subprocess.PIPE, stderr = subprocess.PIPE, shell=True)
                if thung.stdout.readline().decode('utf-8'):
                    print("\rsaw apologies, cache in "+unquote(litty.strip())+" not found", end='')
                    return 5
                else:
                    theng = subprocess.Popen("grep -e "+rer+" buffer.txt", stdout=subprocess.PIPE, stderr = subprocess.PIPE, shell=True) 
                    if theng.stdout.readline().decode('utf-8'):
                        print("https://cc.bingj.com/cache.aspx?q="+litty) 
                        print("https://cc.bingj.com/cache.aspx?q="+litty, file=wude)
                        wude.close()
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
        fin.close()
        theng = subprocess.Popen("grep -e pdf stri.txt > pdfs.txt", stdout=subprocess.PIPE, stderr = subprocess.PIPE, shell=True).communicate()
        fil = open('pdfs.txt', 'r')
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
