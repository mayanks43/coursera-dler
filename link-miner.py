import os, cookielib, urllib2
from HTMLParser import HTMLParser

# create a subclass and override the handler methods
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
r = opener.open("https://class.coursera.org/compilers/lecture/index")

parser = MyHTMLParser()
parser.feed(r.read())
