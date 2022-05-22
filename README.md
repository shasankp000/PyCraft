# Project Info
  >A Minecraft launcher made in python.

  >This Launcher aims to be the best free minecraft launcher for Linux primarily. Porting to other platforms will be done later.

  >This launcher is not illegal as all files are downloaded from libraries.minecraft.net.

  >Piracy concerned rich people feel free to press the back button on the browser :)
  

# Pycraft 1.03 release

  > Added Fabric installation support.
  >
  > Fixed forge launch issues.
  >
  > Added ely_by login system support, (offline skin support coming soon)
  > 
  > GUI changes.
  > 
  > Tons of bugfixes and performance improvements.
  > 
  > Fps boost is in beta testing mode.
  > 
  > Added an internet speed checker.
 
# Installation script changes

  > Added installation support for java 16 (windows and debian based linux)
  > 
  > Added python installation support (windows and debian based linux. Use this only if you don't    
    have python installed by defualt). 

  
# Privacy updates

  > Passwords are no longer stored in the launcher. Only player uuid, accessToken from auth servers  
    and clientToken is randomly generated on each run, for ely_by logins.



# Features
  >This launcher is based on the Tkinter and minecraft_launcher_lib. It offers mojang login and cracked login.
  
  >Includes a special FPS boost option.
  
  >Includes an in-built toggleable vpn, running through torsocks(Linux)
  
  >To run Tor on windows as a service : https://deepdarkweb.github.io/how-to-install-tor-on-windows-without-the-tor-browser-running-tutorial/

  >**Fps boost has been shifted to beta testing mode. That is , it has been tested with java 16.It is still being tested. Feedback would be most graciously appreciated.**

  
# Installation
  >Run python install.py or python3 install.py(if on linux)
 

  >Then run python pycraft_gui.py or python3 pycraft_gui.py

  >Before starting minecraft, do increase or decrease the ram in the settings, so as to update it in the settings file. Or else an error will pop concerning the         JVM.

  > I will patch this in future releases.

**IMPORTANT**
  >After stopping a download, please press CTRL+C twice. (This will close the launcher as well.)
  >For people who have worked with python, it's an issue where i am unable to close the download thread directly at once by raising the KeyboardInterrupt exception.

  >If download fails, you may need to use a vpn(windows) or enable tor in settings(linux)

  >**Any changes in the settings (be it tor, fps boost, ram change, directory change) will require a launcher reboot(not to be confused with system reboot),        to take effect.**

# Pycraft skins system
  > Pycraft has 3 accounts mode. The mojang account mode(microsoft accounts support coming soon),     
    cracked mode and ely_by login system. For the majority of the people who don't know what that is, 
    it is an alternative minecraft service used by Tlauncher as well, only that their security is better. For this mode, you need to create an account at https://ely.by (2 factor authentication not yet supported), and then enter your username and password and start. Supported for all modes, vanilla, forge and fabric.

   > Ely_by skins are not viewable on all servers, only in singleplayer mode and those servers which  
     use it's services. However to view your skin on all servers you can use a client side mod, https://www.curseforge.com/minecraft/mc-mods/customskinloader/ , usage instructions are given on the page. Officially supported till 1.16.5 but there are release versions for the mod for 1.17 in the files section. Just run this mod one time, close minecraft, go to .minecraft/CustomSkinLoader/CustomSkinLoader.json, open it with any text editor

   from the webiste : "- Q: How can I modify configurations of CustomSkinLoader?

   A: The config file is .minecraft/CustomSkinLoader/CustomSkinLoader.json . Unfortunately, there is no way to modify the CustomSkinLoader configuration file in    
   the game currently, so you need to manually modify it by using a code editor (e.g. VSCode). However, we have a website to modify the configuration file online, 
   you only need to import and modify your current configuration file."

   This mod supports: LittleSkin, BlessingSkin, Elyby, SkinMe, GlitchlessGames skins. Since ely_by is the most popular choice, you can go ahead with this mod.

   And yea this mod has no impact on physical resources, like ram and cpu(I used it a lot of times).

# Why the whole vpn thingy?
  >Sometimes mojang's server, libraries.minecraft.net is not available on some systems (especially for those living in Egypt). To fix this a vpn is used. Now the 
   governement of Egypt has kinda cracked down on openvpn (thanks to one of my testers, i wouldn't have known about it otherwise.), so Tor is the best solution to      that.

# Coming soon:
  >FunMc (my minecraft server's website).
  
  >New microsoft account login system as per the latest changes according to mojang in Minecraft: Java Edition

Below is a video stating how to use PyCraft Launcher(rip my trash pc -- i am still working on the fps boost)

https://youtu.be/8TiDc-Z2MA0

# Project discontinued due to life issues 
  >Sorry guys :(
