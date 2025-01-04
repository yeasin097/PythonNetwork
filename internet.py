import psutil
import time
import os

while(True):
    before = psutil.net_io_counters()
    time.sleep(1)
    after = psutil.net_io_counters()
    receive = (after.bytes_recv - before.bytes_recv)/(1024*1024)
    sent = (after.bytes_sent - before.bytes_sent)/1024
    print(f"Upload Speed: {sent:.1f} KB/s")
    print(f"Download Speed: {receive:.1f} MB/s")
    time.sleep(1)
    if(os.name == 'nt'):
        os.system("cls")
    else:
        os.system("clear")
    