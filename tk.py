import tkinter
import psutil
import time
import requests




def get_network_speed():
    total_net_before = psutil.net_io_counters()
    time.sleep(1)
    total_net_after = psutil.net_io_counters()
    down_speed = (total_net_after.bytes_recv - total_net_before.bytes_recv)/1024
    up_speed = (total_net_before.bytes_sent - total_net_before.bytes_sent)/1024
    return up_speed, down_speed



def speed_updater():
    global speed_running
    # speed_running = True
    if speed_running:
        up_speed, down_speed = get_network_speed()
        display_content.config(text=f"Download Speed: {down_speed:.1f}KB/s \n Upload Speed: {up_speed:.1f}KB/s")
        window.after(1000, speed_updater)

def start_running():
    global speed_running
    speed_running = True
    speed_updater()

def get_and_print_public_ip():
    global speed_running
    speed_running = False
    response = requests.get("https://api.ipify.org/")
    ip_address = response.text
    display_content.config(text=f"Your Public IP: {ip_address}")
    





window = tkinter.Tk()

window.title("Python for Network")
window.geometry("400x100")


display_content = tkinter.Label(window, text="Welcome to the Python for Network")
speed_button = tkinter.Button(window, text="Show Speed", command=start_running)
ip_button = tkinter.Button(window, text="Public IP", command=get_and_print_public_ip)
display_content.pack()
speed_button.pack(side=tkinter.LEFT)
ip_button.pack(side=tkinter.LEFT)




window.mainloop()