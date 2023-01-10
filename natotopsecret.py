import os
from multiprocessing import Process
import sys
import requests
import time
import urllib3
urllib3.disable_warnings()
print("usage python3 natotopsecret.py searchterm domain")
rer = sys.argv[1]
rawr = sys.argv[2]

def taskse():
    thing = requests.get("http://web.archive.org/cdx/search/cdx?url="+rawr+"&output=text&fl=original&collapse=urlkey&matchType=prefix", verify=False)
    if thing.ok:
        stri = "stri.txt"
        fin = open(stri, 'w')
        print(thing.text.strip(), file=fin)
        fil = open(stri, 'r')
        for line in fil:
            thong = requests.get("https://cc.bingj.com/cache.aspx?q="+line, verify=False)
            time.sleep(4)
            if thong.ok:
                buffer = open('buffer.txt', 'w')
                print(thong.text.strip(), file=buffer)
                buffed = open('buffer.txt', 'r')
                for liner in buffed:
                    thung = os.popen("grep -e Apologies buffer.txt")
                    if thung == 1:
                        theng = os.popen("grep -e "+rer+" buffer.txt")
                        if theng != 1:
                            print("http://webcache.googleusercontent.com/search?q=cache:"+liner)
                        else:
                            continue
                    else:
                        continue
            else:
                print("too many requests sent to bing, please wait 5 minutes")
                return 5
    else:
        print("too many requests sent to web.archive.org, please wait 5 minutes")
        return 5                
        
if __name__ == '__main__':
    taskse()
