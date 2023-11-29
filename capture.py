# requires adb installed and emulator running to exec out commands via shell

# Importing required module
import subprocess
import time

while True:
    subprocess.Popen("adb exec-out screencap -p > ./frames/screenshot.png", shell=True)

    print("📸Saving frame.")
    # Wait for 5 seconds
    time.sleep(5)
