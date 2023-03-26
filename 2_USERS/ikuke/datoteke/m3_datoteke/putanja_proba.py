import os
import posixpath
p = "G:\Engineering\Software_Development\python\Tool"
p.replace(os.sep, posixpath.sep)

print (p)




import os
import ntpath
p = "G:\Engineering\Software_Development\python\Tool"
p.replace(os.sep, ntpath.sep)

print (p)