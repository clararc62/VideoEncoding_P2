
import os

print("1-->720p")
print("2-->480p")
print("3-->360x240")
print("4-->160x120")
res = int(input("which resolution do you want?"))

while res>4 or res<1:
    print("Are you kidin' me?")
    res = int(input("which resolution do you want?"))

#change the scale according to what the user chooses
if res==1:
    os.system("ffmpeg -i BBB_cut.mp4 -vf scale=1280:720 BBB_720.mp4")
elif res==2:
    os.system("ffmpeg -i BBB_cut.mp4 -vf scale=640:480 BBB_480.mp4")
elif res==3:
    os.system("ffmpeg -i BBB_cut.mp4 -vf scale=360:240 BBB_360x240.mp4")
else:
    os.system("ffmpeg -i BBB_cut.mp4 -vf scale=160:120 BBB_160x120.mp4")

