'''
THIS PROGRAM HAS BEEN CREATED, MODIFIED, TESTED, ETC BY
BRANDON HENSON FOR ALICIA HENSON 12-18 AS A XMAS PRESENT.
'''

import exifread
import os
import pdb
import shutil
import getpass
username = getpass.getuser()
os.mkdir("C:\\Users\\" + username + "\\Desktop\\" + "Unorganized")
sourceRootFolder = "C:\\Users\\" + username + "\\Desktop\\" + "Unorganized"
targetRootFolder = sourceRootFolder + '\\'+ username + "'s_" + 'Organized_Pics'
input("Put all of your pics in the 'Unorganized' folder that just appeared "
      "on the desktop and press 'ENTER'\n")



def Do(root):
    for dirpath, dirnames, filenames in os.walk(root):
        for f in filenames:
            filepath = dirpath + "\\" + f
            processFile(filepath, f)


def processFile(sourceFilePath, filename):
    targetFolder = getTargetFolder(sourceFilePath, filename)
    processMoveBusiness(sourceFilePath, targetFolder, filename)


def getTargetFolder(filepath, filename):
    currentFile = open(filepath, 'rb')
    tags = exifread.process_file(currentFile)
    shootTimeTag = "EXIF DateTimeOriginal"
    '''shootTimeTag = "EXIF DateTimeDigitized"'''
    if shootTimeTag in tags:
        shootTime = str(tags[shootTimeTag])
        if not shootTime:
            shootTime = "0000:00 0000:0000"
    else:
        shootTime = "0000:00 0000:0000"
        '''#pdb.set_trace()'''

    dateArray = shootTime.split(" ")[0].split(":")
    year = dateArray[0]
    month = dateArray[1]
    if dateArray[1] == '01':
        month = 'Jan'
    elif dateArray[1] == '02':
        month = 'Feb'
    elif dateArray[1] == '03':
        month = 'Mar'
    elif dateArray[1] == '04':
        month = 'Apr'
    elif dateArray[1] == '05':
        month = 'May'
    elif dateArray[1] == '06':
        month = 'Jun'
    elif dateArray[1] == '07':
        month = 'Jul'
    elif dateArray[1] == '08':
        month = 'Aug'
    elif dateArray[1] == '09':
        month = 'Sep'
    elif dateArray[1] == '10':
        month = 'Oct'
    elif dateArray[1] == '11':
        month = 'Nov'
    elif dateArray[1] == '12':
        month = 'Dec'
    return targetRootFolder + "\\" + year + "-" + month


def processMoveBusiness(sourceFilePath, targetFolder, filename):
    targetFolderBackup = targetFolder + "\\backup"
    '''#make sure target folders exits'''
    if not os.path.isdir(targetFolder):
        os.makedirs(targetFolder)

    firstAttemptFilePath = targetFolder + "\\" + filename
    print(firstAttemptFilePath)
    if os.path.isfile(firstAttemptFilePath):
        '''#check if we can move to the backup'''
        attemptToBackupFilePath = targetFolderBackup + "\\" + filename
        if os.path.isfile(attemptToBackupFilePath):
            '''#have the same file in the backup folder'''
            '''#do nothing'''
            print ("------[skip]:" + sourceFilePath)
        else:
            '''#move to backup'''
            if not os.path.isdir(targetFolderBackup):
                os.makedirs(targetFolderBackup)

            shutil.move(sourceFilePath, attemptToBackupFilePath)
            print (">>>>>>[backup]:" + sourceFilePath)

    else:
        '''#normal move'''
        shutil.move(sourceFilePath, firstAttemptFilePath)
        print ("[move]:" + sourceFilePath)


Do(sourceRootFolder)
