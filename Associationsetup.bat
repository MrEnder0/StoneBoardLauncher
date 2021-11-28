set "PATH=%UTIL_DIR%;%PATH%"

assoc .sbsave=StoneBoardSave
assoc .sbtheme=StoneBoardTheme

ftype StoneBoardSave="C:\Users\Owner\AppData\Local\Programs\Python\PYTHON36\python.exe" "C:\Users\Owner\Desktop\StoneBoardLauncher-main\importManager.py" "%1" %*
ftype StoneBoardTheme="C:\Users\Owner\AppData\Local\Programs\Python\PYTHON36\python.exe" C:\Users\Owner\Desktop\StoneBoardLauncher-main\importManager.py" "%1" %*
