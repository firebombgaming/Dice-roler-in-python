import os
import random

def one():
	print(" _____")
	print("|     |")
	print("|  0  |")
	print("|_____|")

def two():
	print(" _____")
	print("|0    |")
	print("|     |")
	print("|____0|")

def three():
	print(" _____")
	print("|0   |")
	print("|  0 |")
	print("|___0|")

def four():
	print(" _____")
	print("|0   0|")
	print("|     |")
	print("|0___0|")

def five():
	print(" _____")
	print("|0   0|")
	print("|  0  |")
	print("|0___0|")

def six():
	print(" _____")
	print("|0 0 0|")
	print("|     |")
	print("|0_0_0|")

os.system("clear")

num = random.ranint(1,6)

if num ==1:
	os.system("clear")
	one()
if num ==2:
	os.system("clear")
	two()
if num ==3:
	os.system("clear")
	three()
if num ==4:
	os.system("clear")
	four()
if num ==5:
	os.system("clear")
	five()
if num ==6:
	os.system("clear")
	six()
