from tkinter import Canvas, PhotoImage, Button, Entry, Tk

import tkinter as tk
from tkinter.ttk import Combobox, Progressbar, Frame, Label
from tkinter.messagebox import showerror, showinfo, showwarning, askquestion
from tkvideo import tkvideo
import os
import subprocess
import time
import minecraft_launcher_lib
from minecraft_launcher_lib.forge import install_forge_version, run_forge_installer, supports_automatic_install
import uuid
import platform
from ttkbootstrap import Style
import json
import sys
from threading import Thread
import time
import speedtest



style = Style(theme="cosmo") #Sets the theme of the comboboxes and progressbar. Cosmo is a light-blue theme


'''def get_size(bytes, suffix="B"):
    #Found this on some website, i don't remember now. Used to get the total ram in GB.
    """ 
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


svmem = psutil.virtual_memory()





#Generates the settings.json file which is afterwards read by the settings window. Very important for the program to run

settings = {
            "User-info" : [
                {
                    "username": None,
                    "password": None,
                    "AUTH_TYPE": None,
                }
            ],
            "PC-info" : [
                {
                    "OS": platform.platform(),
                    "Total-Ram": f"{get_size(svmem.total)}",
                }
            ],
            "Minecraft-home" : mc_dir,
            "Show-Snapshots" : False,
            "Fps-Boost" : False,
            "Tor-Enabled" : False,
            "setting-info" : [
                {
                    "snap_selected" : False,
                    "fps_boost_selected" : False,
                    "tor_enabled_selected" : False,
                    "allocated_ram_selected" : None
                }
            ],
            "allocated-ram" : None
        }


if not os.path.exists(r"{}/settings.json".format(currn_dir)):
    with open("settings.json", "w") as js_set:
        json.dump(settings, js_set, indent=4)
        js_set.close()
else:
    pass'''


currn_dir = os.getcwd()
mc_dir = r"{}/.minecraft".format(currn_dir)

with open("settings.json", "r") as js_read:
    s = js_read.read()
    s = s.replace('\t','')  #Trailing commas in dict cause file read problems, these lines will fix it.
    s = s.replace('\n','')  #Found this on stackoverflow.
    s = s.replace(',}','}')
    s = s.replace(',]',']')
    data = json.loads(s)
    #print(json.dumps(data, indent=4,))

os_name = data["PC-info"][0]["OS"]
username = data["User-info"][0]["username"]
password = data["User-info"][0]["password"]
mc_dir = data["Minecraft-home"]
auth_type = data["User-info"][0]["AUTH_TYPE"]
allocated_ram = data["allocated_ram"]
allocated_ram_selected = data["setting-info"][0]["allocated_ram_selected"]
jvm_args = data["jvm-args"]


print(os_name)



if os.path.exists(r"{}/.minecraft".format(currn_dir)):
    print("Existing minecraft installation, checking for versions...")

else:
     os.mkdir(".minecraft")
     os.chdir(".minecraft")
     os.mkdir("versions")

print("**IMPORTANT**")
print("After exiting launcher window, please press CTRL+C in terminal to exit.")
print("After stopping a download, please press CTRL+C twice. (This will close the launcher as well.)")
print("For people who have worked with python, it's an issue where i am unable to close the download thread directly at once by raising the KeyboardInterrupt exception.")
print("")
print("If download fails, you may need to use a vpn(windows) or enable tor in settings(linux)")


class Pycraft():
    global data
    global currn_dir
    global allocated_ram

    

    def __init__(self):

        self.os_name = data["PC-info"][0]["OS"]
        self.username = data["User-info"][0]["username"]
        self.password = data["User-info"][0]["password"]
        self.mc_dir = data["Minecraft-home"]

        self.window = style.master
        
        self.Tk_Width = 1270
        self.Tk_Height = 736

        self.window.geometry("1270x736+110+60")
        self.window.title("Pycraft beta 1.02")

        self.x_Left = int(self.window.winfo_screenwidth()/2 - self.Tk_Width/2)
        self.y_Top = int(self.window.winfo_screenheight()/2 - self.Tk_Height/2)

        self.window.geometry(f"+{self.x_Left}+{self.y_Top}")


        self.window.configure(bg = "#ffffff")
        self.canvas = Canvas(
            self.window,
            bg = "#ffffff",
            height = 736,
            width = 1270,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file = f"img/background.png")
        self.background = self.canvas.create_image(
            635.0, 368.0,
            image=self.background_img)

        self.entry0_img = PhotoImage(file = f"img/img_textBox0.png")
        self.entry0_bg = self.canvas.create_image(
            128.5, 464.0,
            image = self.entry0_img)

        self.entry0 = Entry(
            bd = 0,
            bg = "#c4c4c4",
            font = ("Segou Print", 16),
            highlightthickness = 0)

        self.entry0.insert(0, f"{self.username}")

        self.entry0.place(
            x = 30.0, y = 430,
            width = 197.0,
            height = 66)

        self.entry1_img = PhotoImage(file = f"img/img_textBox1.png")
        self.entry1_bg = self.canvas.create_image(
            475.5, 464.0,
            image = self.entry1_img)

        self.entry1 = Entry(
            bd = 0,
            bg = "#c4c4c4",
            show = ".",
            font = ("Segou Print", 16),
            highlightthickness = 0)

        self.entry1.insert(0,f"{self.password}")

        self.entry1.place(
            x = 377.0, y = 430,
            width = 197.0,
            height = 66)

        self.img0 = PhotoImage(file = f"img/img0.png")
        self.b0 = Button(
            image = self.img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.handle_run,
            relief = "flat")

        self.b0.place(
            x = 690, y = 573,
            width = 257,
            height = 76)

        self.img1 = PhotoImage(file = f"img/img1.png")
        self.b1 = Button(
            image = self.img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.handle_download,
            relief = "flat")

        self.b1.place(
            x = 971, y = 569,
            width = 257,
            height = 76)

        self.img2 = PhotoImage(file = f"img/img2.png")
        self.b2 = Button(
            image = self.img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.config_window,
            relief = "flat")

        self.b2.place(
            x = 1181, y = 0,
            width = 89,
            height = 73)



        self.canvas.create_text(
            125.5, 401.0,
            text = "Username",
            fill = "#000000",
            font = ("Segoe Print", int(16.0)))

        self.canvas.create_text(
            465.5, 398.0,
            text = "Password",
            fill = "#000000",
            font = ("Segoe Print", int(16.0)))

        self.vanilla_version_list = minecraft_launcher_lib.utils.get_available_versions(mc_dir)

        self.forge_version_list = minecraft_launcher_lib.forge.list_forge_versions()




        self.forge_versions = []

        self.versions = []
        

        for i in self.vanilla_version_list:
            self.versions.append((i["type"], i["id"]))

        for j in self.forge_version_list:
            self.forge_versions.append(j)


        self.fversionsList = Combobox(self.window, width=25)
        self.fversionsList.place(x=920, y=450)
        self.fversionsList["values"] = self.forge_versions
        self.fversionsList["state"] = "readonly"
        self.fversionsList.current(0)

        self.fversionsList.bind('<<ComboboxSelected>>')

        self.versionsList = Combobox(self.window, width=25)
        self.versionsList.place(x=220, y=610)
        self.versionsList["values"] = self.versions
        self.versionsList["state"] = "readonly"
        self.versionsList.current(0)

        self.versionsList.bind('<<ComboboxSelected>>')

        self.options = ("mojang login", "cracked login")
        self.options_dl = ("Vanilla", "Forge")


        self.canvas.create_text(
            60, 580,
            text = "Accounts",
            fill = "#000000",
            font = ("Segoe Print", int(16.0)))

        self.canvas.create_text(
            750, 398.0,
            text = "Download/Run Options",
            fill = "#000000",
            font = ("Segoe Print", int(16.0)))

        self.canvas.create_text(
            1000, 398.0,
            text = "Forge Versions",
            fill = "#000000",
            font = ("Segoe Print", int(16.0)))

        self.canvas.create_text(
            300, 580,
            text = "Vanilla Versions",
            fill = "#000000",
            font = ("Segoe Print", int(16.0)))

        

        self.selected_download = tk.StringVar()
        self.download_options = Combobox(self.window, textvariable=self.selected_download, width=25)
        self.download_options["values"] = self.options_dl
        self.download_options["state"] = "readonly"
        self.download_options.place(x=650, y=450)
        self.download_options.current(0)

        self.download_options.bind('<<ComboboxSelected>>')
        
        self.selected_option = tk.StringVar()
        self.acc_options = Combobox(self.window, textvariable=self.selected_option)
        self.acc_options["values"] = self.options
        self.acc_options["state"] = "readonly"
        self.acc_options.place(x=10, y=610)

        self.acc_options.bind('<<ComboboxSelected>>')

        self.window.resizable(False, False)
        self.window.mainloop()
    
    def printProgressBar(self, iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
        """
        Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
            printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
        """
        self.percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        self.filledLength = int(length * iteration // total)
        self.bar = fill * self.filledLength + '-' * (length - self.filledLength)
        print('\r%s |%s| %s%% %s' % (prefix, self.bar, self.percent, suffix), end=printEnd)
        # Print New Line on Complete
        if iteration == total:
            print()


    def maximum(self, max_value, value):
        self.max_value[0] = value

    def run_mc(self):
        '''Runs minecraft with the specifed version'''
        self.login_method = self.acc_options.get()
        self.detected_ver = ""  # yet another small hack
        self.runtime_ver = self.download_options.get()
        global data

        with open("settings.json", "r") as js_read1:
            self.s1 = js_read1.read()
            self.s1 = self.s1.replace('\t','')  #Trailing commas in dict cause file read problems, these lines will fix it.
            self.s1 = self.s1.replace('\n','')  #Found this on stackoverflow.
            self.s1 = self.s1.replace(',}','}')
            self.s1 = self.s1.replace(',]',']')
            self.data1 = json.loads(s)
            #print(json.dumps(data, indent=4,))
            
        self.mc_dir = data["Minecraft-home"]

        self.fps_boost = self.data1["Fps-Boost"]
        self.fps_boost_selected = self.data1["setting-info"][0]["fps_boost_selected"]

        self.ram_gb = int(allocated_ram//1000)
        print(allocated_ram)
        self.cpu_count = os.cpu_count()

        if self.fps_boost and self.fps_boost_selected == True:
            if self.ram_gb > 6:
                self.j1 = f"-XX:+UnlockExperimentalVMOptions -d64, Xmx{self.ram_gb}G -Xms128M XX:ParallelGCThreads={(self.cpu_count)*2} -XX:+AggressiveOpts -XX:+AggressiveHeap"
            else:
                self.j1 = f"-XX:+UnlockExperimentalVMOptions -d64 Xmx{self.ram_gb}G -Xms128M XX:ParallelGCThreads={(self.cpu_count)*2} -XX:+AggressiveOpts -XX:+AggressiveHeap"
        else:
            self.j1 = f"-d64 -Xmx{self.ram_gb}G -Xms128M"


        data["jvm-args"] = self.j1

        with open("settings.json", "w") as js_set:
            json.dump(data, js_set, indent=4)
            js_set.close()

        if self.runtime_ver == "Vanilla": #Checking for selected version before running minecraft.
            if self.login_method == "mojang login":
                try:
                    self.usr = self.entry0.get()
                    self.pwd = self.entry1.get()
                    self.mc_ver = self.versionsList.get()
                        
                    # This is done to get only the version number, cutting out the rest of the string including whitespace

                    if self.mc_ver.startswith("release"):
                        self.detected_ver = self.mc_ver.strip("release ")
                    elif self.mc_ver.startswith("snapshot"):
                        self.detected_ver = self.mc_ver.strip("snapshot ")
                        
                        
                    data["User-info"][0]["username"] = self.usr
                    data["User-info"][0]["password"] = self.pwd
                    data["User-info"][0]["AUTH_TYPE"] = self.acc_options.get()

                    with open("settings.json", "w") as js_set:
                        json.dump(data, js_set, indent=4)
                        js_set.close()


                    self.login_data = minecraft_launcher_lib.account.login_user(self.usr, self.pwd)


                    self.options = {
                    "username": self.login_data["selectedProfile"]["name"],
                    "uuid": self.login_data["selectedProfile"]["id"],
                    "token": self.login_data["accessToken"],
                    "jvmArguments": self.j1,
                    "executablePath": self.data1["executablePath"] #The path to the java executable
                    #"executablePath" : executablePath
                    }

                    self.window.withdraw()
                    self.minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(self.detected_ver, self.mc_dir, self.options)
                    print(f"Launching minecraft version {self.mc_ver}")
                    subprocess.call(self.minecraft_command)
                except minecraft_launcher_lib.exceptions.VersionNotFound as e:
                    showerror(title="Error!", message=e)

            elif self.login_method == "cracked login":
                try:
                    self.usr = self.entry0.get()
                    self.pwd = self.entry1.get()
                    self.mc_ver = self.versionsList.get()
                        
                    if self.mc_ver.startswith("release"):
                        self.detected_ver = self.mc_ver.strip("release ")
                    elif self.mc_ver.startswith("snapshot"):
                        self.detected_ver = self.mc_ver.strip("snapshot ")


                    data["User-info"][0]["username"] = self.usr
                    data["User-info"][0]["password"] = self.pwd
                    data["User-info"][0]["AUTH_TYPE"] = self.acc_options.get()

                    with open("settings.json", "w") as js_set:
                        json.dump(data, js_set, indent=4)
                        js_set.close()

                    self.options = {
                    "username": self.usr,
                    "uuid": uuid.uuid4().hex, #A random UUID generator.
                    "token": "",
                    "jvmArguments": [self.j1],
                    "executablePath": self.data1["executablePath"]
                    #"executablePath" : executablePath
                    }

                    self.window.withdraw()
                    self.minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(self.detected_ver, self.mc_dir, self.options)
                    print(f"Launching minecraft version {self.mc_ver}")
                    subprocess.call(self.minecraft_command)

                except minecraft_launcher_lib.exceptions.VersionNotFound as e:
                    showerror(title="Error!", message=e)
            
        elif self.runtime_ver == "Forge":
            if self.login_method == "mojang login":
                try:
                    self.usr = self.entry0.get()
                    self.pwd = self.entry1.get()
                    self.mc_ver = self.fversionsList.get()
                        
                    # This is done to get only the version number, cutting out the rest of the string including whitespace
                        
                    # Not required while running forge
                    #self.detected_ver1 = 
                    
                    data["User-info"][0]["username"] = self.usr
                    data["User-info"][0]["password"] = self.pwd
                    data["User-info"][0]["AUTH_TYPE"] = self.acc_options.get()

                    with open("settings.json", "w") as js_set:
                        json.dump(data, js_set, indent=4)
                        js_set.close()


                    self.login_data = minecraft_launcher_lib.account.login_user(self.usr, self.pwd)


                    self.options = {
                    "username": self.login_data["selectedProfile"]["name"],
                    "uuid": self.login_data["selectedProfile"]["id"],
                    "token": self.login_data["accessToken"],
                    "jvmArguments" : self.j1,
                    "executablePath": self.data1["executablePath"]
                    #"executablePath" : executablePath
                    }
                    
                    self.window.withdraw()

                    self.minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(self.mc_ver, self.mc_dir, self.options)
                    print(f"Launching minecraft version {self.mc_ver}")
                    subprocess.call(self.minecraft_command)

                except minecraft_launcher_lib.exceptions.VersionNotFound as e:
                    showerror(title="Error!", message=e)
                    print(e)

            elif self.login_method == "cracked login":
                self.usr = self.entry0.get()
                self.pwd = self.entry1.get()
                self.mc_ver = self.fversionsList.get()
                    
                try:
                    if self.mc_ver.startswith("release"):
                        self.detected_ver = self.mc_ver.strip("release ")
                    elif self.mc_ver.startswith("snapshot"):
                        self.detected_ver = self.mc_ver.strip("snapshot ")


                    data["User-info"][0]["username"] = self.usr
                    data["User-info"][0]["password"] = self.pwd
                    data["User-info"][0]["AUTH_TYPE"] = self.acc_options.get()

                    with open("settings.json", "w") as js_set:
                        json.dump(data, js_set, indent=4)
                        js_set.close()

                    self.options = {
                    "username": self.usr,
                    "uuid": uuid.uuid4().hex,
                    "token": "",
                    "jvmArguments" : self.j1,
                    "executablePath": self.data1["executablePath"]
                    #"executablePath" : executablePath
                    }

                    self.window.withdraw()

                    self.minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(self.mc_ver, self.mc_dir, self.options)
                    print(f"Launching minecraft version {self.mc_ver}")
                    subprocess.call(self.minecraft_command)
                except minecraft_launcher_lib.exceptions.VersionNotFound as e:
                    showerror(title="Error!", message=e)
                    print(e)

    def download(self):
        '''Downloads minecraft with the specified version'''
        self.dl_opt = self.download_options.get()
        self.selected_ver = ""
        self.detected_ver1 = ""  # yet another small hack

        self.max_value = [0]

        self.callback = {
            "setStatus": lambda text: print(text),
            "setProgress": lambda value: self.printProgressBar(value, self.max_value[0]),
            "setMax": lambda value: self.maximum(self.max_value, value)
        }

        if self.dl_opt == "Vanilla":
            self.selected_ver = self.versionsList.get()

            if self.selected_ver.startswith("release"):
                    self.detected_ver1 = self.selected_ver.strip("release ")
            elif self.selected_ver.startswith("snapshot"):
                    self.detected_ver1 = self.selected_ver.strip("snapshot ")

            try:
                showinfo(title="Installation started...", message=f"Installing minecraft version {self.selected_ver}")
                minecraft_launcher_lib.install.install_minecraft_version(self.detected_ver1,self.mc_dir, callback=self.callback)
                    
            except:
                showerror(title="Error", message="Errors encountered while installing...")
        elif self.dl_opt == "Forge":
            self.selected_ver = self.fversionsList.get()
                
            if supports_automatic_install(self.selected_ver):
                try:
                    showinfo(title="Installation started..", message=f"Installing forge version {self.selected_ver}")
                    install_forge_version(self.selected_ver, self.mc_dir, callback=self.callback)
                except:
                    showerror(title="Error", message="Errors encountered while installing...")
                    
            else:
                try:
                    showinfo(title="Installation started..", message=f"Installing forge version {self.selected_ver}")
                    run_forge_installer(self.selected_ver)
                except:
                    showerror(title="Error", message="Errors encountered while installing...")
        

    def config_window(self):
        '''A small hack to prevent messing up of the canvas in the settings window.'''
        if self.os_name.startswith("Linux"):
            with open("settings.sh", "w") as f:
                f.write("python3 setting_window.py")
                f.close()
            os.system("chmod 700 settings.sh")
            os.system("./settings.sh")
        elif self.os_name.startswith("Windows"):
            with open("settings.bat", "w") as f:
                f.write("python setting_window.py")
                f.close()
            os.system("settings.bat")



        
    def start_download(self):
        '''Initiates a second window consisting of the download progressbar, while hiding the previous one.'''
        
        def close():
            '''restores the minimized original window and cancels the download.'''
            res = askquestion(title='Abort?', message="Really cancel the download?")
            if res == "yes": 
                try:
                    if self.dl_thread.is_alive():
                        self.window.deiconify()
                        self.pw.destroy()
                except tk.TclError:
                    print("Download window closed.")
            elif res == "no":
                pass
            

        self.window.withdraw()
        self.pw = tk.Toplevel()
        self.pw.geometry("1024x768")
        self.pw.title("Installation window")
        self.pw.configure(bg = "#ffffff")
        self.pw.resizable(False,False)
        self.canvas1 = Canvas(
            self.pw,
            bg = "#3a3a3a",
            height = 768,
            width = 1024,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas1.place(x = 0, y = 0)
        try:
            self.pw.wm_protocol("WM_DELETE_WINDOW", lambda:close())
        except tk.TclError():
            print("Download window closed.")

        self.l1 = Label(self.pw)
        self.l1.place(x=0, y=0)    
        self.player = tkvideo(r"{}/img/progressbar.mp4".format(currn_dir), self.l1, loop=1, size=(1024,500))

        self.b4 = Button(self.pw, text="Stop Download", command = close)
        self.b4.place(x=450, y=600)

        self.pb = Progressbar(self.pw, value=0, style='success.Striped.Horizontal.TProgressbar', length=1000, mode="indeterminate")
        self.pb.place(x=10, y=570)
        
        self.t1 = Thread(target=lambda: self.player.play())
        self.t1.start()

        
    def stop_download(self):
        '''restores the minimized original window and cancels the download.'''
        self.pb.stop()
        self.window.deiconify()
        self.pw.destroy()
        print("Download terminated")
        #raise KeyboardInterrupt

    def handle_progress(self):
        '''handles the progress bar increment'''
        self.pb.start(1)

    def handle_download(self):
        '''Starts the download thread'''
        self.start_download()

        q1 = askquestion(title="Start?", message="Start the download?")
        if q1 == "yes":
   
            try:
                self.t2 = Thread(target=self.handle_progress)
                self.t2.start()

                self.dl_thread = Thread(target=self.download) # Download thread
                self.dl_thread.start() 

                self.monitor(self.dl_thread)
            except KeyboardInterrupt:
                self.dl_thread.join(timeout=4.0)
                self.t2.join(timeout=6.0)
                self.t1.join(timeout=8.0)
            

            print("Download Started.")

        elif q1 == "no":
            try:
                self.stop_download()
                showinfo(title="Aborted", message="Cancelled the download" )
            except tk.TclError:
                self.stop_download()
                showinfo(title="Aborted", message="Cancelled the download" )
        

    def monitor(self, dl_thread):
        '''Monitors the download thread, and updates the progressbar'''
        if self.dl_thread.is_alive():
            self.window.after(100, lambda: self.monitor(self.dl_thread))
        else:
            showinfo(title="Success!", message="Download Completed.")
            self.stop_download()


    def handle_run(self):
        '''Creates the thread on which minecraft is running'''
        self.t4 = Thread(target=self.run_mc)
        self.t4.start()

        self.monitor_mc(self.t4)

    def monitor_mc(self, t4):
        '''Monitors the thread on which minecraft is running'''
        if self.t4.is_alive():
            self.window.after(100, lambda: self.monitor_mc(self.t4))
        else:
            t4.join(timeout=3.0)
            self.window.deiconify()

if __name__ == "__main__":
    try:
        Pycraft()
    except KeyboardInterrupt:
        print("Program Exited")
else:
    sys.exit(1)