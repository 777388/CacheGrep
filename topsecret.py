import os
from multiprocessing import Process
import sys
import subprocess
print("usage python3 topsecret.py searchterm")
rer = sys.argv[1]
import contextlib
import time

def taskse():
    for i in range(255):
        for n in range(255):
            for k in range(255):
                for d in range(255):
                    thing = requests.get("http://web.archive.org/cdx/search/cdx?url="+str(i)+"."+str(n)+"."+str(k)+"."+str(d)+"&output=text&fl=original&collapse=urlkey&matchType=prefix", verify=False)
                    time.sleep(4)
                    stri = "stri.txt"
                    f = open(stri, 'w')
                    print(thing.text.strip(), file=f)
                    fil = open(stri, 'r')
                    for line in fil:
                        thong = requests.get("http://webcache.googleusercontent.com/search?q=cache:"+line, verify=False)
                        time.sleep(1)
                        if thong:
                            buffer = open('buffer.txt', 'w')
                            print(thong.text.strip(), file=buffer)
                            buffed = open('buffer.txt', 'r')
                            for liner in buffed:
                                thung = os.popen("grep 404 buffer.txt")
                                
                                if thung:
                                    break
                                else:
                                    theng = os.popen("grep "+rer+" buffer.txt")
                                    if theng:
                                        print("http://webcache.googleusercontent.com/search?q=cache:"+liner)
                        

if __name__ == '__main__':
    with contextlib.redirect_stdout(None):
        taskse()
