import time  #for time intervals
import psutil #for battery status
from plyer import notification # For receiving desktop notification

#-----Danny Codes-----

#Function gets called in a 20 minute gap(customisable)
def update(battery):
             #sends out notification
            notification.notify(
                #title of the notification,
                title = "BATTERY UPDATE",
                #the body of the notification
                message = "Battery Percentage is " + str(battery),  
                #creating icon for the notification
                #we need to download a icon of ico file format
                app_icon = r'C:\Users\vigo4\Desktop\Projects\My Python quickies\Desktop Battery Notifier\battery_80.ico',
                # the notification stays for 5sec
                timeout  = 2
            )

while True:   
# Gets Battery information   
 battery = psutil.sensors_battery()       
# calls the function  
 update(battery.percent)
#  calls the function with a gap of 20 minutes(customisable)
 time.sleep(60*20)



  

#To run code in background
# python desktop_battery_notifier.py &

# P.S
# I left some ICO images in the folder you could use to give some style to your notification. Enjoy!