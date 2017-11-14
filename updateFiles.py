
from zipfile import ZipFile
import os

def updateVersion(programmName):

    dirNameServer = "\\\\SI-VPROVKOV\\SimpleHTTPServer\\" + programmName
    dirNameClient = '.\\'
    #print dirName

    try:
        newFiles = os.listdir(dirNameServer)
    except:
        print "\nBAD NAME OF PROGRAMM: %s\n" % programmName
        return 0
    print("Files, wich need update: ")
    print(newFiles)

##-------------------------------------------

    # fTest = open(dirNameServer+"\\header.pyc", 'r')
    # fTest.readlines(10)
    # fTest.close()
    #
    # import requests
    # import urllib
    # req2 = urllib.urlopen('http://10.76.18.219:4242/esppTaskTracker/updateFiles.pyc')
    #
    # resp = req2.read()
    # print resp
    # # print req.text
    # fTest = open("test.pyc",'w')
    # fTest.writelines(resp)
    # fTest.close()

##-------------------------------------------

    ##---- contain library.zip in this folder?
    try:
        checkZip = 'library.zip' in os.listdir(dirNameClient)
        ###--- if cant find library.zip - go upper
        if not (checkZip):
            print("Can't find 'library.zip' in %s, try to check to upper folder" % dirNameClient)
            dirNameClient = "." + dirNameClient
            checkZip = 'library.zip' in os.listdir(dirNameClient)
    ##--- if can't find directory, go upper
    except WindowsError:
        print("Can't find 'library.zip' in %s, try to check to upper folder" % dirNameClient)
        dirNameClient ="." + dirNameClient

        try:
            checkZip = 'library.zip' in os.listdir(dirNameClient)
        except WindowsError:
            print("Can't find 'library.zip' in %s" % dirNameClient)
            return 0
    except:
        print("Unrecognize error")
        return 0


    oldFiles = os.listdir(dirNameClient)
    # print(oldFiles)

    ##---- try open 'library.zip', exit if error
    try:
        ZipIn = ZipFile(dirNameClient+'library.zip', 'r')
    except:
        print "Can't find 'library.zip' in directory %s" % dirNameClient
        return 0

    ##---- create new zip-file without files which need to remove
    ZipOut = ZipFile(dirNameClient+'library2.zip', 'w')
    for item in ZipIn.infolist():
        buf = ZipIn.read(item.filename)
        if not (item.filename in newFiles):
            ZipOut.writestr(item, buf)

    ZipIn.close()

    ##------ add new files in ZIP-file
    for itemName in newFiles:
        ZipOut.write(dirNameServer + "\\" + itemName, itemName)

    ZipOut.close()

    ##--- try to backup. If file library_Backup.zip exist - need remove it
    try:
        os.rename(dirNameClient+'library.zip', dirNameClient+'library_Backup.zip')
        print 'Backuping is good'
    except:
        print 'Backup was recreated...'
        os.remove(dirNameClient+'library_Backup.zip')
        os.rename(dirNameClient+'library.zip', dirNameClient+'library_Backup.zip')
        print 'Backuping is good'

    ##--- rename new zip file. If file library.zip is exist - remove it
    try:
        os.rename(dirNameClient+'library2.zip', dirNameClient+'library.zip')
        print 'Rename good'
    except:
        print 'library.zip recreated'
        os.remove(dirNameClient+'library.zip')
        os.rename(dirNameClient+'library2.zip', dirNameClient+'library.zip')
        print 'Rename good'

    print "DONE"
