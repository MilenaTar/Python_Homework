import random
from texttable import Texttable

def intro_func():
    list1 = [[0,1,2],[3,4,5],[6,7,8]]
    t = Texttable()
    t.add_rows(list1)
    print("We will play with  board sized 3x3\n")
    print(t.draw())

def for_3_list(l:list):
    new_list =[]
    list3 = l[:3]
    list4 = l[3:6]
    list5 =l[6:]
    tup = (list3,list4,list5)
    for i in tup:
        new_list.append(i)
    t = Texttable()
    t.add_rows(new_list)
    print(t.draw())


def condition_func(list11:list) -> str:
    #horizonakani hamar
    if list11[0] == list11[1] and list11[1] == list11[2] and list11[2] == user:
        return "Wins user"
    elif list11[0] == list11[1] and list11[1] == list11[2] and list11[2] == comp:
        return "Winc computer"
    elif list11[3] == list11[4] and list11[4] == list11[5] and list11[5] == user:
        return "Wins user"
    elif list11[3] == list11[4] and list11[4] == list11[5] and list11[5] == comp:
        return "Wins computer"
    elif list11[6] == list11[7] and list11[7] == list11[8] and list11[8] == user:
        return "Wins user"
    elif list11[6] == list11[7] and list11[7] == list11[8] and list11[8] == comp:
        return "Wins computer"

#uxxahayaci hamar
    elif list11[0] == list11[3] and list11[3] == list11[6] and list11[6] == user:
        return "Wins user"
    elif list11[0] == list11[3] and list11[3] == list11[6] and list11[6] == comp:
        return "Wins computer"
    elif list11[1] == list11[4] and list11[4] == list11[7] and list11[7] == user:
        return "Wins user"
    elif list11[1] == list11[4] and list11[4] == list11[7] and list11[7] == comp:
        return "Wins computer"

    elif list11[2] == list11[5] and list11[5] == list11[8] and list11[8] == user:
        return "Wins user"

    elif list11[2] == list11[5] and list11[5] == list11[8] and list11[8] == comp:
        return "Wins computer"


#xachadzev
    elif list11[0]== list11[4] and list11[4] == list11[8] and list11[8] == user:
        return "Wins user"
    elif list11[0]== list11[4] and list11[4] == list11[8] and list11[8] == comp:
        return "Wins computer"

    elif list11[2] == list11[4] and list11[4] == list11[6] and list11[6] == user:
        return "Wins user"
    elif list11[2] == list11[4] and list11[4] == list11[6] and list11[6] == comp:
        return "Wins computer" 
    elif  " " not in list11:
        return "Tie!"


intro_func()
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
