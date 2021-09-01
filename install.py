import os
import time
import platform

print("Getting necessary stuff...")
time.sleep(5)
os_name = platform.platform()
if os_name.startswith("Linux"):
    os.system("clear")
    os.system("python3 -m pip install -r requirements.txt")
    os.system("sudo apt-get install gksudo fonts-symbola autoconf automake libtool gcc tor gtk2-engines-murrine -y")
    os.system("git clone https://git.torproject.org/torsocks.git") # Fix for torsocks syscall issue 217
    os.chdir("torsocks")
    os.system("./autogen.sh")
    os.system("./configure")
    os.system("make")
    os.system("sudo make install")
    os.system("clear")
    os.system("sudo rm -r torsocks")
    os.system("cd -")
    print("All requirements installed. Run pycraft_gui.py now to run the launcher.")
elif os_name.startswith("Windows"):
    os.system("cls")
    os.system("pip install -r requirements.txt")
    print("All requirements installed. Run pycraft_gui.py now to run the launcher.")

