#!/usr/bin/env python

## Install Python3 pip Modules

## Python3 (pip)
## pip3 install cfscrape
## pip3 install beautifulsoup4
## pip3 install lxml

import re
import cfscrape
from bs4 import BeautifulSoup

## User input
URL = input("\033[1;32m Enter a URL : \033[1;m")

SCRAPER = cfscrape.create_scraper()
CFURL = SCRAPER.get(URL).content
SOUP = BeautifulSoup(CFURL, "lxml") #html.parser
for link in SOUP.findAll('a', attrs={'href': re.compile("^(http|https)://")}):

    urls = link.get("href")
    #print(urls)
    print('\033[1;33m %s \033[1;m' %urls)
