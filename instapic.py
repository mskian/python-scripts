#!/usr/bin/env python

## Instagram Post Image Downloader
## Install Python pip Modules

# Python2 (pip)
## pip install wget
## pip install beautifulsoup4
## pip install lxml

# Python3 (pip)
## pip3 install wget
## pip3 install beautifulsoup4
## pip3 install lxml

from bs4 import BeautifulSoup
import wget

try: #python3
    from urllib.request import urlopen
except: #python2
    from urllib2 import urlopen
    input = raw_input

## User input
url = input("\033[1;32mEnter a Instagram Post URL : \033[1;m")

insta_post = urlopen(url)
bs = BeautifulSoup(insta_post , "lxml")

## Find Insta Post Image
metatag = bs.find("meta", {"property": "og:image"})

if metatag is not None:

    print (metatag["content"])
    print ("\n")

    print ("Image Started Downloading.......")

    ## Download Image via Wget
    filename = wget.download(metatag["content"])
    print ("\n")

    print ("Done")
    print ("\n")

else:
    print ("Error")
