#!/usr/bin/python
from subprocess import call
import os
def ensure_dir(f):
    if not os.path.exists(f):
        os.makedirs(f)
course = raw_input()
#print course
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
            call(["mv", course+"/"+video_id.strip()+".mp4", course+"/"+video_name.strip()+".mp4"])
            call(["mv", course+"/"+video_name.strip()+".mp4", course+"/"+current_folder+"/"])
    except EOFError:
        break
