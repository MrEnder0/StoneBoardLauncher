from launcher import *
from config import *
import dload
import shutil
import os

if CheckForUpdates == True:
    startLauncher()
    if Experintal == True:
        shutil.rmtree("experimental")
        os.remove('experimental.zip')
        time.sleep(0.5)
        dload.save_unzip("https://github.com/MrEnder0/StoneBoardPackages/archive/refs/heads/experimental.zip")
        source = 'experimental/StoneBoardPackages-experimental'
        dest = 'experimental/StoneBoardPackagesexperimental'
        os.rename(source, dest)
        from experimental.StoneBoardPackagesexperimental.home import *
        startHome()
    else:
        shutil.rmtree("stable")
        os.remove('stable.zip')
        time.sleep(0.5)
        dload.save_unzip("https://github.com/MrEnder0/StoneBoardPackages/archive/refs/heads/stable.zip")
        source = 'stable/StoneBoardPackages-stable'
        dest = 'stable/StoneBoardPackagesstable'
        os.rename(source, dest)
        from stable.StoneBoardPackagesstable.home import *
        startHome()
        
elif CheckForUpdates == False:
    if Experintal == True:
        from experimental.StoneBoardPackagesexperimental.home import *
        startHome()
    else:
        from stable.StoneBoardPackagesstable.home import *
        startHome()
        
else:
    print("Err you can only set CheckForUpdates to True or False or to 1 or 0")
    time.sleep(3)
    quit()
