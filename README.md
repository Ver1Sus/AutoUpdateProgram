# AutoUpdateProgram
 
 I use this program to check autoupdate of python program, which was compiled in *.exe and using library.zip as source of code.
 If program need update - you need just put in library.zip new *.pyc files, and program was update.
 To do this automaticaly, I wrote this program.
 
 Steps:

1) Programm connect to server and check the verion of server-program in 'version.py', like:
      EsppTaskTracker = 1.3
     
2) Program check the version of client program in file 'version.txt', like:
      EsppTaskTracke=1.0
      
3) If version on server larger than client version - need update program. 
4) Load all *.pyc files from server and put it on ./files/
5) Create backup of librrary.zip to library_backup.zip
6) Put all files from ./files/ to library.zip
7) Restart client program
8) PROFIT!

P.S. the idea of auto-updating already in use in my repo: https://github.com/Ver1Sus/Py2exePatch 


Dependencies:
 1) reqests - to connect to server
 2) zipfile - to open library.zip
