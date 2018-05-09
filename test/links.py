#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
#import urllib2
import re # Module for RegEx
import yaml
import cfscrape

def getLinks(url):
     # Get the text at the set URL
    scraper = cfscrape.create_scraper()
    cfurl = scraper.get(url).content
    #html_page = urllib2.urlopen(cfurl)
    soup = BeautifulSoup(cfurl)
    links = ['Full Web Page Internal & External links']
 

    for link in soup.findAll('a', attrs={'href': re.compile("^(http|https)://")}):
        links.append(link.get('href'))
    return links

#print (getLinks("https://example.com"))

## Output printed in result.yml file
with open('result.yml', 'w') as yaml_file:
 yaml.safe_dump((getLinks('https://www.example.com')), yaml_file, default_flow_style=False, encoding='utf-8', allow_unicode=True)


print "done"
