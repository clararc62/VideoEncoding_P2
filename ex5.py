
#SCRIPT TO CALL ALL THE OTHER EXERCISES

ex = int(input("Which exercise do you want to execute? (1,2,3,4)"))

while ex>4 or ex<1:
    print("Try again bro")
    ex = int(input("Which exercise do you want to execute? (1,2,3,4)"))

if ex==1:
    print("You have chosen exercise 1 :)")
    print("Now we will cut the selected time of the BBB video")
    import ex1
    print("Congratulations, you have created the BBB_cut.mp4 video")

elif ex==2:
    print("You have chosen exercise 2 :)")
    print("Now a script that extracts the YUV histogram from the BBB_cut video will be created")
    import ex2
    print("Congratulations, you have created the BBB_ex2.mp4 video")

elif ex==3:
    print("You have chosen exercise 3 :)")
    print("Now you are able to choose the resolution of the new video")
    import ex3
    print("Congratulations, you have created a video with lower resolution")

elif ex==4:
    print("You have chosen exercise 4 :)")
    print("Now you are able to choose")
    import ex4
    print("Congratulations, you have created a new video")

