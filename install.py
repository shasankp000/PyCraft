import os
import time
import platform
import getpass
import time

print("Getting necessary stuff...")
time.sleep(5)
os_name = platform.platform()
usr_accnt = getpass.getuser()
currn_dir = os.getcwd()
py_ver = platform.python_version()


if os_name.startswith("Linux"):
    os.system("clear")
    os.system("python3 -m pip install -r requirements.txt")
    os.system("sudo apt-get install gksudo fonts-symbola autoconf automake libtool gcc tor gtk2-engines-murrine python3 -y")
    os.system("git clone https://git.torproject.org/torsocks.git") # Fix for torsocks syscall issue 217
    os.chdir("torsocks")
    os.system("./autogen.sh")
    os.system("./configure")
    os.system("make")
    os.system("sudo make install")
    os.system("clear")
    os.system("sudo rm -r torsocks")
    os.system("cd -")
    os.system("clear")
    import wget
    print("Installing Java 17.......")
    #wget.download("https://download.java.net/java/GA/jdk13.0.2/d4173c853231432d94f001e99d882ca7/8/GPL/openjdk-13.0.2_linux-x64_bin.tar.gz", bar=wget.bar_adaptive)
    os.system("sudo apt install openjdk-17-jdk -y")
    print("All requirements installed. Run pycraft_gui.py now to run the launcher.")
elif os_name.startswith("Windows"):
    os.system("cls")
    os.system("pip install -r requirements.txt")
    os.system("cls")
    os.chdir(r"C:\\Users\\{}\\Downloads\\ ".format(usr_accnt))
    import wget
    print("Do you want to install python? It is necessary for the launcher to run. (y/n)")
    c1 = ("Enter y if you don't have python installed, n if you have it already : ")
    if c1 == "y":
        print("Installing python 3.9.6.....")
        wget.download("https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe", bar=wget.bar_adaptive)
        filename = wget.detect_filename("https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe")
        os.system(filename)
        time.sleep(5)
        os.remove(filename)
    else:
        os.system("cls")
        print("Installing java 17.....")
        wget.download("https://download.bell-sw.com/java/17.0.3+7/bellsoft-jdk17.0.3+7-windows-amd64.msi", bar=wget.bar_adaptive)
        filename = wget.detect_filename("https://download.bell-sw.com/java/17.0.3+7/bellsoft-jdk17.0.3+7-windows-amd64.msi")
        os.system(f"msiexec /i {filename}")
    time.sleep(5)
    os.remove(f"{filename}")
    print("Creating desktop shortcut.....")
    os.chdir(r"C:\\Users\\{}\\Desktop\\ ".format(usr_accnt))
    os.system(f"shortcut.exe /F:Pycraft.lnk /A:C /T:{currn_dir}\\pycraft_gui.py /W:{currn_dir}")
    os.system("cls")
    print("You can set the icon of the shortcut with the icon in pycraft's folder.")
    print("All requirements installed. Run pycraft_gui.py now to run the launcher.")

