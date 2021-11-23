
import os

print("1-->change from stereo to mono")
print("2-->mute second channel")
print("3-->mute first channel")
print("4-->switch the two audio channels")
print("5-->change audio codec to mp3")

hi = int(input("what do you want?"))
while hi>5 or hi<1:
    print("C'mon")
    hi = int(input("what do you want?"))

#convert to mono
if hi==1:
    os.system("ffmpeg -i BBB_cut.mp4 -ac 1 BBB_mono.mp4")

#to mute the first channel and keep the second:
elif hi==2:
    os.system("ffmpeg -i BBB_cut.mp4 -map_channel -1 -map_channel 0.1.0 -c:v copy BBB_leftmute.mp4")

#to mute the second channel and keep the first:
elif hi==3:
    os.system("ffmpeg -i BBB_cut.mp4 -map_channel 0.1.0 -map_channel -1 -c:v copy BBB_rightmute.mp4")

#switch the two audio channels:
elif hi==4:
    os.system("ffmpeg -i BBB_cut.mp4 -map_channel 0.1.1 -map_channel 0.1.0 -c:v copy BBB_channelswitch.mp4")

#change audio codec to mp3
else:
    os.system("ffmpeg -i BBB_cut.mp4 -vcodec copy -acodec mp3 BBB_audiocodec.mp4")


