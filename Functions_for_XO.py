from texttable import Texttable
def intro_func():
	'''
	Introduse the board to a user.
	'''
    list1 = [[0,1,2],[3,4,5],[6,7,8]]
    t = Texttable()
    t.add_rows(list1)
    print("We will play with  board sized 3x3")
    print(t.draw())

def for_3_list(l:list):
''' 
Prints the board every round.
Parameters:
l - list
'''
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
	'''
	Cheks the conditions so that we can choose who is the winner .
	Parameter
	list11 - list
	Returns a string
	'''
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

        