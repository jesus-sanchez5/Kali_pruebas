from plyer import notification
import psutil, os

battery = psutil.sensors_battery()
percentage = battery.percent
mensaje = str(battery.percent)
notification.notify(title='Bateria',message=mensaje,app_icon=None,timeout=20)
print(f"Our system has {percentage} percent ")

