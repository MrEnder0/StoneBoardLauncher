from packageManager import *
from launcher import *
from config import *

dpackage = threading.Thread(target=downloadPackage, args=(1,), daemon=True)
dpackage.start()
startLauncher()
