import os
from multiprocessing import Process
import sys
import requests
import time
print("usage python3 natotopsecret.py searchterm domain")
rer = sys.argv[1]
rawr = sys.argv[2]

def taskse():
    thing = requests.get("http://web.archive.org/cdx/search/cdx?url="+rawr+"&output=text&fl=original&collapse=urlkey&matchType=prefix", verify=False)
    stri = "stri.txt"
    fin = open(stri, 'w')
    print(thing.text.strip(), file=fin)
    fil = open(stri, 'r')
    for line in fil:
        thong = requests.get("http://webcache.googleusercontent.com/search?q=cache:"+line, verify=False)
        time.sleep(4)
        if thong:
            buffer = open('buffer.txt', 'w')
            print(thong.text.strip(), file=buffer)
            buffed = open('buffer.txt', 'r')
            for liner in buffed:
                theng = os.popen("grep "+rer+" buffer.txt")
                if theng:
                    print("http://webcache.googleusercontent.com/search?q=cache:"+liner)
                else:
                    break
                        

if __name__ == '__main__':
    taskse()
