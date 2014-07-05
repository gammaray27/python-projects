import sys
import time

desc = ''' Mewtwo has challenged all the Greatest Pokemon 
trainers to a pokemon battle'''

print(desc)

accept = input("do you accept? ")

if accept == "yes":
	print("there is a mostorous storm up ahead, you have")
	print("a trustworthy Blastoise")
else:
	sys.exit()

move1 = input("you see a large rock  ahead, you can move up, down left or right. ")

if move1 == "up":
	print("Blastoise narrowly avoids wrecking and gets you to")
	print("the surface just in time")
	time.sleep(3)
else:
	print("you crash into the rock and black out... you wake up on an island beach 2 days later")
	time.sleep(5)
	sys.exit()
print("you have made it to new island, you decide to rest for a minute")
time.sleep(3)
print("after your rest you decide to enter a gigantic building")

