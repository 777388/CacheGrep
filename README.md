# CacheGrep
GREP caches of Waybackurls


MYTHICAL works best, the others are sometimes a bit buggy having to deal with rate limiting and pool processing.

FULL IP RANGE USAGE
python3 topsecret.py searchterm

(!!!FASTER!!!) python3 UMBRA.py searchterm outputfilename  (!!!!Be sure to set!!! ulimit -Sn unlimited)

DOMAIN NAME USAGE

python3 natotopsecret.py searchterm domain

FILE UPLOAD USAGE

(!!!FASTER!!!!) python3 MAJESTIC.py searchterm filename (!!!!Be sure to set!!! ulimit -Sn unlimited)

Google Bypass, Passive recon on site

(!!!!FASTEST!!!!) python3 MYTHICAL.py searchterm Domain (!!!!Be sure to set!!! ulimit -Sn unlimited; and apply xs and c_name cookies from facebook)

!grabs a proxy list from https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt

!Proxy hops every request

!URLEncodes for google cache system

!Hops through Bing

!Automatically determines if theres a captcha page and avoids it hopping again

!Determines if the items not found, kept in a few buffers

!.1 second wait times between requests, 10 reqs a second per thread determined by your computers pool

!Only saves URLS of items that contain the words you grep into a file called domain.output.txt

!!!!!FEEL FREE TO EDIT AND CHANGE AS YOU'D LIKE!!!!!!

!!!!!!!!!!!!I DONT KNOW ABOUT LICENSING!!!!!!!!!!!!!!

You may want to # out the wait timers, they seem to be going slower than .1 though they work for safety
