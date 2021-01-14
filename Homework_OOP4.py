import os
def smth():
	path = os. getcwd()
	print(path)
	print(os.listdir(path))
	choice1 = input("You need to choose to open txt file or to go another directory. \n [open or go]: ")
	if choice1 == "open":
		text = open("text.txt","r")
		print (text.read())
		text.close()
	else:
		os.mkdir("Dir1")
		os.chdir("Dir1")
		os.mkdir("Dir2")
		os.mkdir("Dir3")
		os.chdir("Dir3")
		os.mkdir("Dir4")
	choice2 = input("Do you want to  delete the folders? \n [Yes/No] : ")
	if choice2 == "Yes":
		os.rmdir("Dir4")
		os.chdir("..")
		os.rmdir("Dir3")
		os.rmdir("Dir2")
		os.chdir("..")
		os.rmdir("Dir1")


smth()