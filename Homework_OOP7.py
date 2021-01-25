import random
import logging

logging.basicConfig(filename= "Log_Example.txt", filemode = "w",level=logging.DEBUG)
for i in range(10):
	num = random.randint(0,50)
	if num in range(0,10):
		print(num)
		logging.debug(F'number is in 0-9:{num}') 
	if num in range(10,20):
		print(num)
		logging.info(F"Number is in 10-19: {num}")
	if num in range(20,30):
		logging.warning(F"Number is in 20-29: {num}")
	elif num in range(30,40):
		logging.error(F"Number is in 30-39: {num}")
	elif num in range(40,51):
		logging.critical(F"Number is in 40-49:{num}")
