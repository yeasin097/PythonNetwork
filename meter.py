import psutil
import time
from threading import Thread
from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw


class NetworkSpeedMonitor:
    def __init__(self):
        self.download_speed = 0
        self.upload_speed = 0
        self.running = True

    def get_network_speed(self):
        """Continuously measure upload and download speed."""
        while self.running:
            counters_1 = psutil.net_io_counters()
            time.sleep(1)  # Measure speed over 1 second
            counters_2 = psutil.net_io_counters()
            self.download_speed = (counters_2.bytes_recv - counters_1.bytes_recv) / 1024  # KB/s
            self.upload_speed = (counters_2.bytes_sent - counters_1.bytes_sent) / 1024  # KB/s
            print(f"Download: {self.download_speed:.1f} KB/s, Upload: {self.upload_speed:.1f} KB/s")

    def stop(self):
        self.running = False


def create_image(text):
    """Create an icon image with text."""
    width, height = 64, 64
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    draw.text((5, 5), text, fill="black")
    return image


def update_icon(icon, monitor):
    """Update the icon with the latest network speed."""
    while monitor.running:
        text = f"D: {monitor.download_speed:.1f}KB/s\nU: {monitor.upload_speed:.1f}KB/s"
        icon.icon = create_image(text)
        time.sleep(1)


def main():
    monitor = NetworkSpeedMonitor()

    # Start network monitoring in a separate thread
    monitor_thread = Thread(target=monitor.get_network_speed, daemon=True)
    monitor_thread.start()

    # Create and run the system tray icon
    icon = Icon("Internet Speed Monitor")
    icon.menu = Menu(
        MenuItem("Exit", lambda: (monitor.stop(), icon.stop()))
    )
    icon.icon = create_image("Loading...")
    icon.visible = True

    # Update the icon with speeds
    icon_updater = Thread(target=update_icon, args=(icon, monitor), daemon=True)
    icon_updater.start()

    icon.run()


if __name__ == "__main__":
    main()
