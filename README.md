# PyCraft
  >A Minecraft launcher made in python.
  >The main objective of this launcher is to enable players to enjoy minecraft (especially those without a mojang/microsoft account). 
  >This launcher is not illegal as all files are downloaded from libraries.minecraft.net
  

# Features
  >This launcher is based on the Tkinter and minecraft_launcher_lib. It offers mojang login and cracked login.
  >Includes a special FPS boost option.
  >Includes an in-built toggleable vpn, running through torsocks(Linux)
  >To run Tor on windows as a service : https://deepdarkweb.github.io/how-to-install-tor-on-windows-without-the-tor-browser-running-tutorial/
  
# Installation
  >Run python install.py or python3 install.py(if on linux)
  >Then run python pycraft_gui.py or python3 pycraft_gui.py

**IMPORTANT**
  >After exiting launcher window, please press CTRL+C in terminal to exit.
  >After stopping a download, please press CTRL+C twice. (This will close the launcher as well.)
  >For people who have worked with python, it's an issue where i am unable to close the download thread directly at once by raising the KeyboardInterrupt exception.

  >If download fails, you may need to use a vpn(windows) or enable tor in settings(linux)

# Why the whole vpn thingy?
  >Sometimes mojang's server, libraries.minecraft.net is not available on some systems (especially for those living in Egypt). To fix this a vpn is used. Now the 
   governement of Egypt has kinda cracked down on openvpn (thanks to one of my testers, i wouldn't have known about it otherwise.), so Tor is the best solution to      that.

# Coming soon:
  >FunMc (my minecraft server's website) and it's API for skin systems and capes (absolutely free)
  >New microsoft account system as per the latest changes according to mojang in Minecraft: Java Edition
