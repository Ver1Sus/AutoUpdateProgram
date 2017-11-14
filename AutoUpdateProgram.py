import requests, updateFiles

_ProgrammName = "EsppTaskTracker"




print "Checking the version..."

##--- parse the file 'version.txt' in folder with programm.
    ## Save the number of current version in var 'currentVersion'.
    ## Make it = '1.0' if not founded in file
currentVersion="1.0"
try:
    versionFile = open("version.txt", "r")
    line=" "
    while line != "":
        line = versionFile.readline()
        if line.split('=')[0] == 'currentVersion':
            currentVersion = line.split('=')[1].replace("\"", "")
            break
    versionFile.close()
except:
    print "Can't find 'version.txt' on directory with program. Creating new file 'version.txt'"

print "Your version: " + currentVersion


##--- try connect to server and get the version
    ## Make server version equal to current version if server is unavailable,
    ## or the name of programm not founded
serverVersion = currentVersion
try:
    url = "http://10.76.18.219:4242/version.py"
    req = requests.get(url, timeout=2)
except:
    print "Can't check new version of programm"
##--- Connecting is done, check version
else:
    ##----save result in text
    versions = req.text
    if str(req.status_code) != '200':
        print req.status_code

    ##----- and parse the result text, find version
    versions = versions.split('\n')
    for version in versions:
        if version.split('=')[0] == _ProgrammName:
            serverVersion = version.split('=')[1].replace("\"", "")
            break

    print "Server version: " + serverVersion

    ##--- If server have new version - update the programm on PC and update file version.txt
    if float(currentVersion) >= float(serverVersion):
        print "\nUpdating not needed\n"
    else:
        print "\nNot equal, need update\n"

        ##---- Run script, that will update '*.pyc' files in library.zip
        returnUpdate = updateFiles.updateVersion(_ProgrammName)

        if returnUpdate != 0:
            ##--- update version in file 'version.txt'
            versionFile = open("version.txt", "w")
            line = "currentVersion=\"%.1f\"" % float(serverVersion)
            print line
            versionFile.write(line)
            versionFile.close()
            print ("*"*16)
            print("PROGRAM UPDATED, NEED RESTART PROGRAM")
            print ("*" * 16)
            raw_input("Press Enter to exit...")
            exit()
        else:
            print("Program was not updated")

print "\nStart programm"





