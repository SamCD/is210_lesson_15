import urllib2
from bs4 import BeautifulSoup

URL = 'http://www.whitehouse.gov/net-neutrality'
DATA = urllib2.urlopen(URL).read()
HTML_SOUP = BeautifulSoup(DATA)

def obama_net_neutrality():
    links=soup.findAll('p','tt')
    for link in links:
        print link

if __name__ == '__main__':
    # You can use this conditional block for debugging
    # print HTML_SOUP
    pass
