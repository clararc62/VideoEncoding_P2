import subprocess
from datetime import time

#ask to the user
min = int(input("Which is the minute start?"))
sec=int(input("Which is the sec start?"))

# time(hour, minute and second)
start_time = time(hour = 0, minute = min, second = sec)

#encode 12 seconds of the video starting at the time specified by the user
subprocess.call(["ffmpeg", "-i", "BBB.mp4", "-ss", str(start_time), "-t", "00:00:12", "-async", "1", "-c", "copy" ,"BBB_cut.mp4"])
