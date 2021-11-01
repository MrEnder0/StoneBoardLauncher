from config import *
import threading
import shutill
import pygame
import dload
import os

def(downloadPackage):
  packagesDownloaded = False
  if CheckForUpdates == True:
    if Experintal == True:
        source = "experimental/StoneBoardPackages-experimental"
        dest = "experimental/StoneBoardPackagesexperimental"
        #delete old packages without error
        try:
            os.remove("experimental.zip")
        except OSError:
            pass
        try:
            shutil.rmtree("experimental")
        except OSError:
            print("No packages found making new ones")
            pass
        
        print("Installing new experimental packages")
        time.sleep(0.5)
        dload.save_unzip("https://github.com/MrEnder0/StoneBoardPackages/archive/refs/heads/experimental.zip")
        os.rename(source, dest)
        packagesDownloaded = True
    else:
        source = "stable/StoneBoardPackages-stable"
        dest = "stable/StoneBoardPackagesstable"
        #delete old packages without error
        try:
            os.remove("stable.zip")
        except OSError:
            print("No packages found making new ones")
            pass
        try:
            shutil.rmtree("stable")
        except OSError:
            pass
        
        print("Installing new stable packages")
        time.sleep(0.5)
        dload.save_unzip("https://github.com/MrEnder0/StoneBoardPackages/archive/refs/heads/stable.zip")
        os.rename(source, dest)
        packagesDownloaded = True
        
elif CheckForUpdates == False:
    if Experintal == True:
      packagesDownloaded = True
    else:
      packagesDownloaded = True
        
else:
    print("Err you can only set CheckForUpdates to True or False or to 1 or 0")
    time.sleep(3)
    quit()

