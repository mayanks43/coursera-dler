#!/usr/bin/python
from subprocess import call
import os
def ensure_dir(f):
    if not os.path.exists(f):
        os.makedirs(f)

course = raw_input()
ensure_dir(course)
current_folder = "default"
f = None
while True:
    try:
        x = raw_input()
        if(len(x.split('#')) < 3):
            current_folder = x.strip()
            #print current_folder
            ensure_dir(course+'/'+current_folder)
            f = open(course+'/'+current_folder+'/playlist.m3u','w')
        else:
            stuff = x.split('#')
            video_id, video_name, link = stuff
            f.write(video_name.strip()+".mp4\n")
            #print video_id, video_name, link
            pathto = course+"/"+current_folder+"/"+video_name.strip()+".mp4"
            if not os.path.exists(pathto):            
                call(["wget", "-O", pathto,"--load-cookies=cookies.txt", link.strip()])
            else:
                statinfo = os.stat(pathto)
                if statinfo.st_size == 0:
                    call(["wget", "-O", pathto,"--load-cookies=cookies.txt", link.strip()])
    except EOFError:
        break




