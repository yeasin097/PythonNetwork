import psutil
import time
from tkinter import Tk, Label

def get_network_speed():
    """Calculate upload and download speed."""
    counters_1 = psutil.net_io_counters()
    time.sleep(1)  # Measure the speed over 1 second
    counters_2 = psutil.net_io_counters()
    
    download_speed = counters_2.bytes_recv - counters_1.bytes_recv
    upload_speed = counters_2.bytes_sent - counters_1.bytes_sent
    
    return download_speed / 1024, upload_speed / 1024  # Convert to KB/s

def update_label():
    """Update the label with the current network speeds."""
    download_speed, upload_speed = get_network_speed()
    label.config(text=f"Download: {download_speed:.2f} KB/s\nUpload: {upload_speed:.2f} KB/s")
    root.after(1000, update_label)  # Update every second

# GUI Setup
root = Tk()
root.title("Internet Speed")
root.geometry("200x50")
# root.attributes('-topmost', True)  # Keep the window on top
# root.overrideredirect(True)  # Remove window decorations

# Label to display speed
label = Label(root, text="Calculating...", font=("Helvetica", 10))
label.pack()

update_label()
root.mainloop()
