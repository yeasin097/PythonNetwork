import psutil
import time

while(True):
    before = psutil.net_io_counters()
    time.sleep(1)
    after = psutil.net_io_counters()
    print(before)
    print(after.bytes_recv-before.bytes_recv)
    