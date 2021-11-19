from packageManager import *
from launcher import *
from config import *
import threading

#Download packages in a thread
dpackage = threading.Thread(target=downloadPackage)
dpackage.start()
startLauncher()

#Launch the home after downloading
if Experintal:
  from experimental.StoneBoardPackagesexperimental.home import *
  startHome()
else:
  from stable.StoneBoardPackagesstable.home import *
  startHome()
