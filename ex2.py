import os

#import the histogram to the video considering each frame
os.system("ffmpeg -i BBB_cut.mp4 -vf split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay BBB_ex2.mp4")

