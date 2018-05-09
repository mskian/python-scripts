#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
#import urllib2
import cfscrape
import re
 
#html_page = urllib2.urlopen("https://example.com")

# Get the text at the set URL
scraper = cfscrape.create_scraper()

url = "https://example.com"
cfurl = scraper.get(url).content
soup = BeautifulSoup(cfurl)
for link in soup.findAll('a', attrs={'href': re.compile("^(http|https)://")}):

 ## Print Output
 print link.get('href')
