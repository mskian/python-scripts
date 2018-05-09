#!/usr/bin/env python

## Scrape Internal Links & External Links
## Install Python pip Modules

# Python2 (pip)
## pip install cfscrape
## pip install beautifulsoup4
## pip install lxml

# Python3 (pip)
## pip3 install cfscrape
## pip3 install beautifulsoup4
## pip3 install lxml

#from bs4 import BeautifulSoup
#import cfscrape
#import re

import sys

VER = 2

try:
    if sys.version_info >= (3,0):
        VER = 3
        from bs4 import BeautifulSoup
        import cfscrape
        import re
    else:
        input = raw_input
        from bs4 import BeautifulSoup
        import cfscrape
        import re
except:
        pass
        

## User input
url = input("\033[1;32mEnter a URL : \033[1;m")

scraper = cfscrape.create_scraper()
cfurl = scraper.get(url).content
soup = BeautifulSoup(cfurl, "lxml")
for link in soup.findAll('a', attrs={'href': re.compile("^(http|https)://")}):

 urls = link.get("href")
 print (urls)
 