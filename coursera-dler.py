from subprocess import call
import os
def ensure_dir(f):

    if not os.path.exists(f):
        os.makedirs(f)

course = raw_input()
ensure_dir(course)

while True:
    try:
        x = raw_input().split()
        filename = x[0]
        link = x[1]
        print filename,link
        call(["wget", "-O", course+"/"+filename+".mp4","--load-cookies=cookies.txt", link])
    except EOFError:
        break




