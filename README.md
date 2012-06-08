coursera-dler
=============

Coursera Bulk video download script

A Script to download all videos from a coursera course at one go.

== You will need ==
- Export [Cookies 1.2] (https://addons.mozilla.org/en-US/firefox/addon/export-cookies/) Mozilla add-on
- wget
- python 2.7

== Usage == 
1. First browse and login to the coursera course on your browser (mozilla supported).
2. Get your cookies.txt file and save it in the same directory as where your coursera-dler files are.
3. Make files executable by typing these instructions:
    $ chmod +x coursera-dler.py 
    $ chmod +x link-miner.py 
4. Then run the scripts:
    $ ./link-miner.py | ./coursera-dler.py
    
TODO: Add ability to save state
TODO: Add ability to save in folders


