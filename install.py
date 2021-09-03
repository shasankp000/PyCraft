import os
import time
import platform
import getpass
import shutil



print("Getting necessary stuff...")
time.sleep(5)
os_name = platform.platform()
usr_accnt = getpass.getuser()
currn_dir = os.getcwd()
py_ver = platform.python_version()


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
    print("Patching files...")
    try:
      if os.path.exists("/usr/lib/python3/dist-packages/minecraft_launcher_lib"):
        os.chdir("/usr/lib/python3/dist-packages/minecraft_launcher_lib")
        os.remove("forge.py")
        shutil.copy(f"{currn_dir}/patches/forge.py", "/usr/lib/python3/dist-packages/minecraft_launcher_lib")
    except PermissionError:
      if os.path.exists(r"/home/{}/.local/lib/python3/site-packages/minecraft_launcher_lib".format(usr_accnt)):
        os.chdir(f"/home/{usr_accnt}/.local/lib/python3/site-packages/minecraft_launcher_lib")
        os.remove("forge.py")
        shutil.copy(f"{currn_dir}/patches/forge.py", f"/home/{usr_accnt}/.local/lib/python3/site-packages/minecraft_launcher_lib")
    os.system("sudo rm -r torsocks")
    os.system("cd -")
    print("All requirements installed. Run pycraft_gui.py now to run the launcher.")
elif os_name.startswith("Windows"):
    os.system("cls")
    os.system("pip install -r requirements.txt")
    os.system("cls")
    print("Please replace the python file from the pacthes folder to c:\\users\\<yourname>\\appdata\\local\\programs\\python<version_number>\\site-packages\\minecraft_launcher_lib\\forge.py")
    print("Ignore this message if you are running this program for the first time.")
    print("All requirements installed. Run pycraft_gui.py now to run the launcher.")

