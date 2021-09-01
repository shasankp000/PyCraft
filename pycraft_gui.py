import json 
from ttkbootstrap import Style
from tkinter.ttk import Progressbar
from tkinter.messagebox import askquestion, showinfo
from tkinter import Label, Canvas, PhotoImage
import tkinter as tk
import sys
import os
import time
from threading import Thread
from tkvideo import tkvideo
import platform
import psutil



currn_dir = os.getcwd()
mc_dir = r"{}/.minecraft".format(currn_dir)

def get_size(bytes, suffix="B"):
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
            "Fps-Boost" : False,
            "Tor-Enabled" : False,
            "setting-info" : [
                {
                    "fps_boost_selected" : False,
                    "tor_enabled_selected" : False,
                    "allocated_ram_selected" : 128.0
                }
            ],
            "allocated-ram" : 128.0,
            "jvm-args": None
        }


if not os.path.exists(r"{}/settings.json".format(currn_dir)):
    with open("settings.json", "w") as js_set:
        json.dump(settings, js_set, indent=4)
        js_set.close()
else:
    pass

with open("settings.json", "r") as js_read:
    s = js_read.read()
    s = s.replace('\t','')  #Trailing commas in dict cause file read problems, these lines will fix it.
    s = s.replace('\n','')
    s = s.replace(',}','}')
    s = s.replace(',]',']')
    data = json.loads(s)
    #print(json.dumps(data, indent=4,))

os_name = data["PC-info"][0]["OS"]
username = data["User-info"][0]["username"]
password = data["User-info"][0]["password"]
mc_home = data["Minecraft-home"]
fps_boost = data["Fps-Boost"]
tor_enabled = data["Tor-Enabled"]
fps_boost_selected = data["setting-info"][0]["fps_boost_selected"]
tor_enabled_selected = data["setting-info"][0]["tor_enabled_selected"]

style = Style()


root = style.master
root.configure(bg = "#3a3a3a")
root.title("Pycraft Updater")
root.geometry("761x403+140+50")

Tk_Width = 761
Tk_Height = 403

x_Left = int(root.winfo_screenwidth()/2 - Tk_Width/2)
y_Top = int(root.winfo_screenheight()/2 - Tk_Height/2)

root.geometry(f"+{x_Left}+{y_Top}")


root.resizable(False, False)







canvas = Canvas(
    root,
    bg = "#3a3a3a",
    height = 768,
    width = 1024,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = "img/mc1.png")
background = canvas.create_image(
    380.5,201.5,
    image=background_img)






canvas.create_text(
    395, 350,
    text = "Getting everything ready.....",
    fill = "#c4c4c4",
    font = ("Segou Print", int(16.0)))

canvas.create_text(
    400, 200,
    text = "PyCraft Launcher 1.02",
    fill = "#c4c4c4",
    font = ("Segou Print", int(26.0)))




#l1 = Label(root)
#l1.pack()

#v1 = tkvideo(r"{}/intro_gif.mp4".format(currn_dir), l1, loop=1, size=(640,360))


pb1 = Progressbar(root, value=0, style='info.Horizontal.TProgressbar', length=300, mode="indeterminate")
pb1.place(x=250, y=400)        


t1 = Thread(target=lambda: os.system("./main.sh"))
t2 = Thread(target=lambda: os.system("main.bat"))
#t3 = Thread(target=lambda: v1.play())


def checksettings():
    '''A small hack to check settings and start the launcher accordingly.'''
    if tor_enabled and tor_enabled_selected == True:

            #time.sleep(20.0)
            #pb1.stop()
        if os_name.startswith("Linux"):
            res2 = askquestion(title="Grant permission", message="Grant permission to permform administrative task?")
            if res2 == "yes":
                showinfo(title="Ok", message="Please enter your password in the next window to start tor")
                os.system("gksudo service tor start")
            elif res2 == "no":
                showinfo(title="Abort", message="Tor cannot start without administrative privileges.")
                sys.exit(0)
            with open("main.sh", "w") as f:
                f.write("torsocks python3 main.py")
                f.close()
                os.system("chmod 700 main.sh")
                root.after(23000, lambda:t1.start())
        elif os_name.startswith("Windows"):
            with open("main.bat", "w") as f:
                f.write("python main.py")
                f.close()
                root.after(23000, lambda: t2.start())

    else:
            #time.sleep(20.0)
            #pb1.stop()
        if os_name.startswith("Linux"):
            with open("main.sh", "w") as f:
                f.write("python3 main.py")
                f.close()
            os.system("chmod 700 main.sh")
            root.after(23000, lambda: t1.start())
        elif os_name.startswith("Windows"):
            with open("main.bat", "w") as f:
                f.write("python main.py")
                f.close()
            root.after(23000, lambda: t2.start())




#root.after(1000, lambda:t3.start())
#root.after(2000, lambda:pb1.start())
window_running = True
pb1.start()
checksettings()
#root.after(20000, lambda: pb1.stop())
root.after(24000, lambda: root.withdraw())



if t1.is_alive() or t2.is_alive():
    pb1.stop()

try:
    root.mainloop()
except KeyboardInterrupt:
    print("Program Exited")

