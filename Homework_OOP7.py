import random
import logging

logging.basicConfig(filename= "Log_Example.txt", filemode = "w",format = ' %(message)s time :%(asctime)s',level=logging.DEBUG)
for i in range(10):
	num = random.randint(0,50)
	if num in range(0,10):
		logging.debug(F'Debug message: number is in 0-9:{num}') 
	if num in range(10,20):
		print(num)
		logging.info(F"Infor message: number is in 10-19: {num}")
	if num in range(20,30):
		logging.warning(F"Warning message: number is in 20-29: {num}")
	elif num in range(30,40):
		logging.error(F"Error message: number is in 30-39: {num}")
	elif num in range(40,51):
		logging.critical(F"Critical message: number is in 40-49:{num}")
print("THE END")