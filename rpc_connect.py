import rpc
import time
from time import mktime 

client_id = '883637926255296513'  # Your application's client ID as a string. (This isn't a real client ID)
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)  # Send the client ID to the rpc module




def rpc_connect():

    print("Connecting to rpc, this may take a while.....")
    time.sleep(5)
    start_time = mktime(time.localtime())
    while True:
        activity = {
                "state": "Minecraft",  # anything you like
                "details": "Playing",  # anything you like
                "timestamps": {
                    "start": start_time
                },
                "assets": {
                    #"small_text": "",  # anything you like
                    #"small_image": "",  # must match the image key
                    "large_text": "Pycraft Launcher",  # anything you like
                    "large_image": "minecraft"  # must match the image key
                }
            }
        rpc_obj.set_activity(activity)
        print("Rpc connection successful")
        time.sleep(20)




