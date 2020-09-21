# DeleteFolders
delete all the empty subfolders of a base folder

This little script firstly executes an input where we have to write the full path of the base directory (ex. C:\Users\xxx\Base). 

We want to delete all the empty folders and subfolders inside this base directory.

For that reason we must create a function (drop_empty_folders) that removes all the empty folders.

This function has to be executed same times as the longest subfolder path.

For that reason at the beggining we count the number of directories. We also count the number of files at the beggining and at the end for check reasons.
