__author__ = 'luoguoling'
from HTMLParser import HTMLParser
import sys
class TitleParser(HTMLParser):
    def __init__(self):
        self.title = ''
        self.readingtitle = 0
        HTMLParser.__init__()
    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            self.readingtitle = 1
    def handle_data(self, data):
        #Ordinarily,this is slow
        self.title += data
    def handle_endtag(self, tag):
        if tag == 'title':
            self.readingtitle = 0
    def gettitle(self):
        return self.title
fd = open('a')
tp = TitleParser()
tp.feed(fd.read())
print "Title is:",tp.gettitle()