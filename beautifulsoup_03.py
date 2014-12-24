#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Using bs4 part 2"""

import urllib2
from bs4 import BeautifulSoup

URL = 'http://sps.cuny.edu/whoweare/departments/it'
DATA = urllib2.urlopen(URL).read()
SOUP = BeautifulSoup(DATA)


def sps_it_department():
    """Makes business cards out of SPS IT website"""
    name = []
    direct = []
    names = SOUP.findAll('span',{'class':'name bold'})
    email = SOUP.select('a[href^=mailto]')
    emails = []
    for i in email:
        if i.string != None:
            emails.append(i.string.encode('utf-8').strip())
    for link in names:
         name.append(link.get_text())
    for j,i in enumerate(name):
        last = i.split(",")[0].lstrip()
        first = i.split(",")[1].rstrip()
        direct.append({(last,first): emails[j]})
    print direct
        
if __name__ == '__main__':
    # You can use this conditional block for debugging
    # print SOUP
    pass
