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


#TODO: add ability to specify cookies file and create course folder on demand

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if(tag == 'a' and ('title', 'Video (MP4)') in attrs):
            a = dict(attrs)
            link = a['href']
            name = link.split('?')[1].split('=')[1]
            print name, a['href']
cj = cookielib.MozillaCookieJar()
cj.load(os.path.join("cookies.txt"))
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
r = opener.open("https://class.coursera.org/"+course+"/lecture/index")
print course
parser = MyHTMLParser()
parser.feed(r.read())
