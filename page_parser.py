#!/usr/bin/python
import os, cookielib, urllib2
from HTMLParser import HTMLParser
import argparse
import sys

parser = argparse.ArgumentParser(description='script to mine links from a coursera page')
parser.add_argument('course', type=str, help='course name')

args = parser.parse_args()
if args.course != "":
    course = args.course
else:
    print "Enter course name"
    sys.exit(1)

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def __init__(self, *args, **kwargs):
        HTMLParser.__init__(self, *args, **kwargs)
        self.header = False
        self.lecture = False
        self.lectureid = 0
    def handle_starttag(self, tag, attrs):
        if ('class', 'list_header') in attrs:
            self.header = True
        if ('class', 'lecture-link') in attrs:
            self.lecture = True
            a = dict(attrs)
            link = a['href']
            name = link.split('?')[1].split('=')[1]
            print name+'#',
        if(tag == 'a' and ('title', 'Video (MP4)') in attrs):
            a = dict(attrs)
            link = a['href']
            name = link.split('?')[1].split('=')[1]
            print a['href']
        #print "Encountered a start tag:", tag, attrs
    def handle_endtag(self, tag):
        pass
        #print "Encountered an end tag :", tag
    def handle_data(self, data):
        #print data
        if self.header:
            print data.strip()
            self.header = False
        if self.lecture:
            print data.replace('/','\\').strip()+'#',
            self.lecture = False
print course        
cj = cookielib.MozillaCookieJar()
cj.load(os.path.join("cookies.txt"))
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
r = opener.open("https://class.coursera.org/"+course+"/lecture/index")

parser = MyHTMLParser()

parser.feed(r.read())
