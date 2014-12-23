import urllib2
from bs4 import BeautifulSoup

URL = 'http://sps.cuny.edu/whoweare/departments/it'
DATA = urllib2.urlopen(URL).read()
SOUP = BeautifulSoup(DATA)

def sps_it_department():
    """Makes business cards out of SPS IT website"""
    name = []
    direct = {}
    names = SOUP.findAll('span',{'class':'name bold'})
     for link in names:
         name.append(link.get_text())
    for i in name:
        last = i.split(",")[0].lstrip()
        first = i.split(",")[1].rstrip()
        direct[last] = first
    print direct
        
if __name__ == '__main__':
    # You can use this conditional block for debugging
    # print SOUP
    pass
