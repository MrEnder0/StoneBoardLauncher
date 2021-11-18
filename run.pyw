from packageManager import *
from launcher import *
from config import *
import threading

dpackage = threading.Thread(target=downloadPackage)
dpackage.start()
startLauncher()

if Experintal:
  from experimental.StoneBoardPackagesexperimental.home import *
  startHome()
else:
  from stable.StoneBoardPackagesstable.home import *
  startHome()
