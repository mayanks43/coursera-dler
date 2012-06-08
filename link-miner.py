import os, cookielib, urllib2
from HTMLParser import HTMLParser
course = "compilers"
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
