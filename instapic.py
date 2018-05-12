#!/usr/bin/env python

## Install Python3 pip Modules

# Python3 (pip)
## pip3 install wget
## pip3 install beautifulsoup4
## pip3 install lxml

from urllib.request import urlopen
from bs4 import BeautifulSoup
import wget

## User input
URL = input("\033[1;32mEnter a Instagram Post URL : \033[1;m")

INSTA_POST = urlopen(URL)
BS = BeautifulSoup(INSTA_POST, "html.parser")

## Find Insta Post Image
METATAG = BS.find("meta", {"property": "og:image"})

if METATAG is not None:

    print(METATAG["content"])
    print("Image Started Downloading.......")

    ## Download Image via Wget Method
    FILENAME = wget.download(METATAG["content"])

else:
    print("Error")
