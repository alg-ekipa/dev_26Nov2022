#from pathlib import Path, PureWindowsPath, PurePosixPath
import os
import ntpath

os.system('cls')

absolute_path = os.path.dirname(__file__)
print(absolute_path)
putanja=absolute_path


putanja.replace(os.sep, ntpath.sep)

print (putanja)
