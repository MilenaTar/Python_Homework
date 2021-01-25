#creating json
import json
import requests
import threading

def reading_json(a): 
	with open (F"{a}") as file:
		data = json.load(file)
		return data

def loading_picture(b):
	response = requests.get(b)
	with open(F"sample{len(b)}.pnj", "wb") as pic:
		pic.write(response.content)


for i in reading_json("picture.json"):
	x = threading.Thread(target = loading_picture, args = (i,))
	x.start()




