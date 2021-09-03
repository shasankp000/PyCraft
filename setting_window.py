import tkinter
from tkinter import Canvas, PhotoImage, Button, Entry, Tk, StringVar, DoubleVar
from tkinter.messagebox import showerror, showinfo
from tkinter.ttk import Checkbutton, Scale, Label
from ttkbootstrap import Style
import json
import psutil
import platform
import os
import time


def get_size(bytes, suffix="B"):
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

currn_dir = os.getcwd()
mc_dir = r"{}/.minecraft".format(currn_dir)

with open("settings.json", "r") as js_read:
    s = js_read.read()
    s = s.replace('\t','')  #Trailing commas in dict cause file read problems, these lines will fix it.
    s = s.replace('\n','')
    s = s.replace(',}','}')
    s = s.replace(',]',']')
    data = json.loads(s)
    #print(json.dumps(data, indent=4,))

os_name = data["PC-info"][0]["OS"]
mc_home = data["Minecraft-home"]
fps_boost = data["Fps-Boost"]
tor_enabled = data["Tor-Enabled"]
fps_boost_selected = data["setting-info"][0]["fps_boost_selected"]
tor_enabled_selected = data["setting-info"][0]["tor_enabled_selected"]
allocated_ram = data["allocated_ram"]
allocated_ram_selected = data["setting-info"][0]["allocated_ram_selected"]

style = Style()

window_s = style.master

window_s.geometry("1024x768+130+50")
window_s.configure(bg = "#3a3a3a")
     
Tk_Width = 1024
Tk_Height = 768

x_Left = int(window_s.winfo_screenwidth()/2 - Tk_Width/2)
y_Top = int(window_s.winfo_screenheight()/2 - Tk_Height/2)

window_s.geometry(f"+{x_Left}+{y_Top}")

window_s.title("Pycraft settings")
canvas = Canvas(
    window_s,
    bg = "#3a3a3a",
    height = 768,
    width = 1024,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"img/bg1.png")
background = canvas.create_image(
        500.0, 368.0,
        image=background_img)

canvas.create_text(
    539.5, 45.5,
    text = "SETTINGS",
    fill = "#000000",
    font = ("Segou Print", int(20.0)))

canvas.create_text(
    562.0, 619.0,
    text = "Network Settings",
    fill = "#000000",
    font = ("Segou Print", int(20.0)))

#global variables
cb1 = ""
cb2 = ""
s1 = ""

#Small hack for remembering settings in the gui
if fps_boost_selected == True:
    cb1 = StringVar(value="selected")
else:
    cb1 = StringVar(value="deselected")

if tor_enabled_selected == True:
    cb2 = StringVar(value="selected")
else:
    cb2 = StringVar(value="deselected")




def check2():
    global fps_boost
    global fps_boost_selected
    if cb1.get() == "selected":
        fps_boost = True
        fps_boost_selected = True
        
    elif cb1.get() == "deselected":
        fps_boost = False
        fps_boost_selected = False
        
    
    data["Fps-Boost"] = fps_boost
    data["setting-info"][0]["fps_boost_selected"] = fps_boost_selected


    with open("settings.json", "w") as js_set:
            json.dump(data, js_set, indent=4)
            js_set.close()


def check3():
    global tor_enabled
    global tor_enabled_selected
    if cb2.get() == "selected":
        tor_enabled = True
        tor_enabled_selected = True
        
    elif cb2.get() == "deselected":
        tor_enabled = False
        tor_enabled_selected = False

    data["Tor-Enabled"] = tor_enabled
    data["setting-info"][0]["tor_enabled_selected"] = tor_enabled_selected

    with open("settings.json", "w") as js_set:
            json.dump(data, js_set, indent=4)
            js_set.close()


def save():
    '''Saves the minecraft home dir path, which is entered.'''
    global mc_home
    mc_home = entry0.get()
    data["Minecraft-home"] = mc_home

    with open("settings.json", "w") as js_set:
            json.dump(data, js_set, indent=4)
            js_set.close()


current_value = DoubleVar()

def get_current_value():
    return '{: .2f} MB'.format(current_value.get())

def slider_changed(event):
    global s1
    global value_label
    try:
        value_label.configure(text=get_current_value())
        s1 = get_current_value()
        flt_s1 = float(s1.rstrip(" MB"))
        #print(s1)
        data["setting-info"][0]["allocated_ram_selected"] = flt_s1
    except NameError:
        pass
    
    with open("settings.json", "w") as js_set:
            json.dump(data, js_set, indent=4)
            js_set.close()




sn1 = Checkbutton(window_s, style="info.Roundtoggle.Toolbutton", onvalue="selected", offvalue="deselected", command=check2, variable=cb1)
sn1.place(x=500, y=135.0)

sn2 = Checkbutton(window_s, style="info.Roundtoggle.Toolbutton", onvalue="selected", offvalue="deselected", command=check3, variable=cb2)
sn2.place(x=500, y=680.0)




canvas.create_text(
    152.5, 146.0,
    text = "FPS Boost(experimental - Requires relaunch)",
    fill = "#000000",
    font = ("Segou Print", int(10.0)))

canvas.create_text(
    231.5, 694.0,
    text = "Enable Tor(requires to relaunch)",
    fill = "#000000",
    font = ("Segou Print", int(16.0)))

canvas.create_text(
    300, 225,
    text = "Minecraft Directory(requires to relaunch)",
    fill = "#000000",
    font = ("Segou Print", int(20.0)))

canvas.create_text(
    200.5, 478.0,
    text = "JVM Memory Allocation(requires to relaunch)",
    fill = "#000000",
    font = ("Segou Print", int(16.0)))

canvas.create_text(
    539.5, 430,
    text = "Minecraft-Settings",
    fill = "#000000",
    font = ("Segou Print", int(20.0)))

str_ram = data["PC-info"][0]["Total-Ram"].strip("    GB")
ram = float(str_ram)
med_ram = (ram*1000)/2

slider = Scale(
    window_s,
    from_=128,
    to=ram*1000,
    command=slider_changed,
    style="info.Horizontal.TScale",
    variable=current_value, 
    length = "1000"
)

slider.place(x=5, y=500)



#Very important system check.

first_time_run = True

if allocated_ram and allocated_ram_selected == None:
    #slider.set(allocated_ram_selected)
    first_time_run = True
    #print(first_time_run)
elif allocated_ram and allocated_ram_selected != None:
    slider.set(allocated_ram_selected)
    first_time_run = False
    #print(first_time_run)


current_value_label = Label(
    window_s,
    text='Ram Assigned:',
    style = "info.TLabel",
    background='yellow'
)

current_value_label.place(x=270, y=530)

value_label = Label(
    window_s,
    text=get_current_value(),
    style = "info.TLabel",
    background='yellow'
)
value_label.place(x=370, y=530)

l3 = Label(
    window_s,
    text=f"Total : {ram*1000} MB",
    style = "info.TLabel",
    background='yellow'
)

l3.place(x=460, y=530)

def save_ram():
    global allocated_ram_selected
    global med_ram

    s2 = get_current_value()
    flt_s2 = float(s2.rstrip(" MB"))
    data["allocated_ram"] = flt_s2
    print(flt_s2)

    with open("settings.json", "w") as js_set:
            json.dump(data, js_set, indent=4)
            js_set.close()

    #print(s1)

    if flt_s2>(med_ram):
        slider.set(med_ram)
        showerror(title="Error!", message="Cannot assign more than 50 percent of host OS's ram")
    elif flt_s2<(med_ram):
        slider.set(flt_s2)
        showinfo(title="Done", message=f"Allocated {flt_s2} MB of ram")

entry0_img = PhotoImage(file = f"img/img_textBox3.png")
entry0_bg = canvas.create_image(
    333.5, 300.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    font = ("Segou Print", 20),
    highlightthickness = 0)

entry0.insert(0, f"{mc_home}")

curn_path = entry0.get()

entry0.place(
    x = 60.0, y = 267.0,
    width = 547.0,
    height = 62)

img3 = PhotoImage(file = f"img/img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = save,
    relief = "flat")

b3.place(
    x = 790, y = 267,
    width = 119,
    height = 60)

b4 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = save_ram,
    relief = "flat")

b4.place(
    x = 790, y = 530,
    width = 119,
    height = 60)

window_s.resizable(False, False)
window_s.mainloop()
