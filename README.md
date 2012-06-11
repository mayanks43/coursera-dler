coursera-dler
=============

Coursera Bulk video download script

A Script to download all videos from a coursera course at one go.

== You will need ==
- [Export Cookies 1.2] (https://addons.mozilla.org/en-US/firefox/addon/export-cookies/) Mozilla add-on or [Cookie.txt Export] (https://chrome.google.com/webstore/detail/lopabhfecdfhgogdbojmaicoicjekelh) Chrome add-on
- wget
- python 2.7

== Usage == 

1. First install Export Cookies 1.2 into your firefox
1. First browse and login to the coursera course on your browser (mozilla supported).
2. Get your cookies.txt file and save it in the same directory as where your coursera-dler files are.
3. Make files executable by typing these instructions:  
    $ chmod +x coursera-dler.py  
    $ chmod +x link-miner.py 
4. Then whenever you want to download videos for a particular course, run these commands:
    $ ./link-miner.py coursename | ./coursera-dler.py  
    Specify coursename such as compilers, ml, pgm, etc. without quotes.
5. To stop download just press Ctrl+Z.
6. To continue download, delete the file that was incompletely downloaded last time and use the same command again.
7. Similarly, When new videos are up just run the same command again.
8. Automatically creates playlist of all videos in the order they should be seen.
