'''https://stackoverflow.com/questions/12946384/windows-install-fonts-from-cmd-bat-file/67903796#67903796'''

import os
import subprocess
import time
    
    # vb script template
TEMPL  = """ 
Set objShell = CreateObject("Shell.Application")
Set objFolder = objShell.Namespace("%s")
Set objFolderItem = objFolder.ParseName("%s")
objFolderItem.InvokeVerb("Install")
"""
    
    
vbspath = os.path.join(os.getcwd(), 'fontinst.vbs')
    
for directory, dirnames, filenames in os.walk(os.getcwd()):
    for filename in filenames:
        fpath = os.path.join(directory, filename)
    
        if fpath[-4:] == ".ttf": # modify this line for including multiple extension
            with open(vbspath, 'w') as _f:
                f.write(_TEMPL%(directory, filename))
                subprocess.call(['cscript.exe', vbspath])
                time.sleep(3) # can omit this
                    
os.remove(vbspath)  # clean
