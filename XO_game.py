from Functions_for_XO import *
import random


list11 = [" ",' ',' ',' ',' ',' ',' ',' ',' ']
try:
    user = input("Choose X or O: ")
    if user !="X" or user !="O":
        raise Exception("Thats not a valid value thats why I will choose")
except Exception as e :
    print(e)
    user ="X"
if user == "X":
    comp = "O"
else: 
    comp = "X"
print("user: {}".format(user))
print("comp: {}".format(comp))
c = 1
while " "  in list11:
    user_position = input("Choose position from 0-8: ")
    comp_position = random.randint(0,8)
    print(comp_position)
    while not list11[int(user_position)] == " ":
        user_position = input("This cell is filled, choose another position from 0-8: ")
    list11[int(user_position)] = user
    if condition_func(list11):
        print(condition_func(list11))
        print("The board after {} round".format(c))
        for_3_list(list11)
        break
    while not list11[comp_position] == " ":
        comp_position = random.randint(0,8)
        print('new', comp_position)
    list11[comp_position]= comp
    print("The board after {} round".format(c))
    for_3_list(list11)
    if condition_func(list11):
        print(condition_func(list11))
        break
    c+=1 
