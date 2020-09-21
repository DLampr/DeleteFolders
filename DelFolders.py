#! python3
# coding: utf-8

#Number of directories in base folder

import os

BaseFolder = input('Enter the base folder path here: ')

FilesNum = 0
DirNum = 0

for base, dirs, files in os.walk(BaseFolder):
    for directories in dirs:
        DirNum += 1
    for Files in files:
        FilesNum += 1

#Delete empty folders

def drop_empty_folders(BaseFolder):
    """Verify that every empty folder removed in local storage."""

    for root, dirs, files in os.walk(BaseFolder, topdown=False):
        if not dirs and not files:
            os.rmdir(root)

#the function must be executed same times as count of subfolder paths            

for i in range(DirNum):
    drop_empty_folders(BaseFolder)
    
#check how many empty directories were removed and that no file was deleted

FilesNumAft = 0
DirNumAft = 0

for base, dirs, files in os.walk(BaseFolder):
    for directories in dirs:
        DirNumAft += 1
    for Files in files:
        FilesNumAft += 1

print('Number of files deleted',FilesNum-FilesNumAft) #should always be zero...we dont want any file deleted, just the empty folders
print('Number of Directories deleted',DirNum-DirNumAft)
