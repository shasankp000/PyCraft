import speedtest



class SpeedTracker():
    '''A net speed tracker based on the speedtest-cli module'''
    def __init__(self):
        '''Gets the download speed in Mbit/s'''
        print("Checking the download speed....")
        self.raw_dl_speed = speedtest.Speedtest().download()
        self.rounded_speed = round(self.raw_dl_speed)
        self.finalspeed = self.rounded_speed/(1e+6) 
        
    def get_download_speed(self):
        '''Returns the download speed'''
        print(f"Download Speed : {self.finalspeed} Mbit/s" )
        return f"Download Speed : {self.finalspeed} Mbit/s" 

