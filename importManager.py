import shutil
import time
import sys
import os

currentPath =  os.getcwd()
importData = sys.argv
save = "sbsave"
theme = "sbtheme"

print(importData)

def listToString(importData): 
    str1 = "" 
    for ele in importData: 
        str1 += ele   
    return str1

    cleanedData = listToString(s)
    print(cleanedData)

cleanedData = listToString(importData)

#if save in importData:

shutil.copy(cleanedData, "C:/Users/Owner/Desktop/StoneBoardLauncher-main/storage/servers")

#if theme in importData:
shutil.copy(cleanedData, "C:/Users/Owner/Desktop/StoneBoardLauncher-main/storage/themes")

