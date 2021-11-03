#! python3
# coding: utf-8

import os

BaseFolder = input('Enter the base folder path here: ')

#Number of directories in the base folder
FilesNum = 0
DirNum = 0

for base, dirs, files in os.walk(BaseFolder):
    for directories in dirs:
        DirNum += 1
    for Files in files:
        FilesNum += 1

#Delete empty folders
def drop_empty_folders(BaseFolder):
    """Removes every empty folder inside the BaseFolder"""

    for root, dirs, files in os.walk(BaseFolder, topdown=False):
        if not dirs and not files:
            os.rmdir(root)

#The function must be executed same times as count of subfolder paths            
for i in range(DirNum):
    drop_empty_folders(BaseFolder)
    
#Check how many empty directories were removed and that no file was deleted
FilesNumAft = 0
DirNumAft = 0

for base, dirs, files in os.walk(BaseFolder):
    for directories in dirs:
        DirNumAft += 1
    for Files in files:
        FilesNumAft += 1

print('Number of files deleted',FilesNum-FilesNumAft) #Should be zero...we don't want any files deleted. Just the empty folders.
print('Number of Directories deleted',DirNum-DirNumAft)
