# Project restarted 
  > Contributors to this project will really be appreciated.


# Project Info
  >A Minecraft launcher made in python.

  >This Launcher aims to be the best free minecraft launcher for Linux primarily. Porting to other platforms will be done later.

  >This launcher is not illegal as all files are downloaded from libraries.minecraft.net.

  >Piracy concerned rich people feel free to press the back button on the browser :)
  

# Changelog

  ![Home Tab](img/pycraft1.png)
  ![Installations Tab](img/pycraft2.png)
  ![Settings Tab](img/pycraft3.png)
  ![Additional Settings Tab](img/pycraft4.png)


  >v1.04-beta-2 
  
  > To use the latest version, it's best to clone the project and then run it, since I fail to keep the releases updated in the release section in tandem with 
  the main code folders in the .git
  >
  > Yes, minecraft 1.19 and all subsequent updates are supported.
  >
  > Fixed issue of being unable to play downloaded versions offline without internet.
  >
  > Fixed all bugs on Windows.
  >
  > Rewritten the ram allocation alogrithm, jvm no longer assigns ram by rounding off to the nearest GB. What you select on the slider is what you get.
  >
  > Fixed issue of cracked login in Fabric. Players using cracked mode will now have a permanent UUID generated by the launcher.
  >
  > Changed GUI totally.
  >
  > Ely_by login mode is now optional if customskinloader is used.
  > 
  > GUI changes(Merged all 3 files into one main launcher).
  > 
  > Added a new download mode named (fps clients). This mode will detect custom clients by placing them in the versions folder. I have chosen Ares     client as the candidate for now. This is not fully implemented yet so work in progress
  > 
  > Fps boost is still(sadly) in beta testing mode.
  > 
  > Fixed the download window.
  > 
  > There is a font folder now containing all fonts the launcher uses. There is no copyright on these fonts, and can be used anywhere. Users are needed
  > to install these fonts or else the launcher will not look as it is intended to look.
  > 
  > Added a "Bypass Ram limiter" option which will override Pycraft's defualt settings to allocate only upto 50% of system ram to minecraft. With this
  > option enabled people can set ram more than 50% of the total ram, if needed. 

# Planned Updates

  >Deal with the GUI once and for all
  >
  >Add a new news page on the launcher
  >
  >Add a modinstaller
  >
  >Make a few fps boosting modpacks(tested on my pc gives around 1200 fps without shaders)
  >
  >Rename cracked mode to something better

# Installation script changes

  > Added installation support for java 17 (windows and debian based linux). The launcher only supports this variant of java 17 now. 
  > 
  > Added python installation support (windows and debian based linux. Use this only if you don't    
    have python installed by defualt). 

  
# Privacy updates

  > Passwords are no longer stored in the launcher. Only player uuid, accessToken from auth servers  
    and clientToken is randomly generated on each run, for ely_by logins.
    
  > Players using cracked mode will now have a permanent UUID generated by the launcher on first run in cracked mode



# Features
  >This launcher is based on the Tkinter and minecraft_launcher_lib. It offers mojang login and cracked login.
  
  >Includes a special FPS boost option(old releases).
  
  >Includes an in-built toggleable vpn, running through torsocks(Linux) (old releases)
  
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


