import os
from multiprocessing import Process
import sys
import subprocess
print("usage python3 topsecret.py searchterm")
rer = sys.argv[1]
import contextlib
import time
import urllib3
urllib3.disable_warnings()

def taskse():
    for i in range(255):
        for n in range(255):
            for k in range(255):
                for d in range(255):
                    thing = requests.get("http://web.archive.org/cdx/search/cdx?url="+str(i)+"."+str(n)+"."+str(k)+"."+str(d)+"&output=text&fl=original&collapse=urlkey&matchType=prefix", verify=False)
                    if thing.ok:
                        time.sleep(4)
                        stri = "stri.txt"
                        f = open(stri, 'w')
                        print(thing.text.strip(), file=f)
                        fil = open(stri, 'r')
                        for line in fil:
                            thong = requests.get("https://cc.bingj.com/cache.aspx?q="+line, verify=False)
                            time.sleep(1)
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
                                            continue:
                                    else:
                                        continue
                                else:
                                    continue
                            else:
                                print("Too many requests to bing, please wait 5 minutes")
                                return 5
                    else:
                        print("too many requests to archive, please wait 5 minutes")
                        return 6
if __name__ == '__main__':
    with contextlib.redirect_stdout(None):
        taskse()
