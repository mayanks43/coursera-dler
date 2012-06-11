#!/usr/bin/python
from subprocess import call
import os
def ensure_dir(f):
    if not os.path.exists(f):
        os.makedirs(f)

course = raw_input()
ensure_dir(course)
current_folder = "default"
while True:
    try:
        x = raw_input()
        if(len(x.split('#')) < 3):
            current_folder = x.strip()
            #print current_folder
            ensure_dir(course+'/'+current_folder)            
        else:
            stuff = x.split('#')
            video_id, video_name, link = stuff
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




