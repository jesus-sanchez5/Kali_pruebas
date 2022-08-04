# from plyer import notification
# notification.notify(title='Noti',message='holaaaa',app_icon=None,timeout=20)



# import os

# def notify(title, text):
    # os.system("""
            #   osascript -e 'display notification "{}" with title "{}"'
            #   """.format(text, title))

# notify("Title", "Heres an alert")


import psutil, os
battery = psutil.sensors_battery()
percentage = battery.percent
print(f"Our system has {percentage} percent ")
def notify(title, text):
     os.system("""osascript -e 'display notification "{}" with title "{}"'""".format(text, title))

notify("Title {percentage}", "Heres an alert '{percentage}'")