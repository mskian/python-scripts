#!/usr/bin/env python

#import urllib2
from BeautifulSoup import BeautifulSoup
import cfscrape

# Get the text at the set URL
scraper = cfscrape.create_scraper()

url = "https://example.com"
cfurl = scraper.get(url).content
#bs = BeautifulSoup(urllib2.urlopen(url))
bs = BeautifulSoup(cfurl)

metatag = bs.find("meta", {"property": "og:image"})
if metatag is not None:
    print metatag["content"]
else:
    print "This page has no Open Graph meta image tag"
