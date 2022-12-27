from tkinter import *
from tkinter.messagebox import showinfo
from itertools import permutations

y=""
x = 2
player_1 = []
player_2 = []

def define_sign(number):
    global x, y
    global player_1,player_2

    set1=permutations([1,2,3])
    set2=permutations([3,5,7])
    set3=permutations([1,5,9])
    set4=permutations([4,5,6])
    set5=permutations([7,8,9])
    set6=permutations([1,4,7])
    set7=permutations([2,5,8])
    set8=permutations([3,6,9])

    for i in set1,set2,set3,set4,set5,set6,set7,set8:
        for j in list(i):
            player1 = all(ele in player_1 for ele in j)
            player2 = all(ele in player_2 for ele in j)

            if player1 == True:
                print(" Player 1 Wins the game ! ")
                showinfo(" Game Result: ", " Player 1 Wins the game!")
                break

            elif player2 == True:
                print(" Player 2 Wins the game ! ")
                showinfo(" Game Result: ", " Player 2 Wins the game! ")
                break
            
            else:
                #showinfo(" Game Result: ", " No-One Wins the game! ")
                break
                
    

    if number==1:
        if x%2==0:
            y='X'
            player_1.append(number)
            print(player_1)

        elif x%2!=0:
            y='O'
            player_2.append(number)
            print(player_2)
        b1.config(text=y)
        x=x+1

    if number == 2:
        if x%2 == 0:
            y = 'X'
            player_1.append(number)
            print(player_1)

        elif x%2 != 0:
            y = 'O'
            player_2.append(number)
            print(player_2)
        b2.config(text=y)
        x=x+1

    if number == 3:
        if x%2 == 0:
            y = 'X'
            player_1.append(number)
            print(player_1)

        elif x%2 != 0:
            y = 'O'
            player_2.append(number)
            print(player_2)
        b3.config(text=y)
        x=x+1

    if number == 4:
        if x%2 == 0:
            y = 'X'
            player_1.append(number)
            print(player_1)

        elif x%2 != 0:
            y = 'O'
            player_2.append(number)
            print(player_2)
        b4.config(text=y)
        x=x+1

    if number == 5:
        if x%2 == 0:
            y = 'X'
            player_1.append(number)
            print(player_1)

        elif x%2 != 0:
            y = 'O'
            player_2.append(number)
            print(player_2)
        b5.config(text=y)
        x=x+1

    if number == 6:
        if x%2 == 0:
            y = 'X'
            player_1.append(number)
            print(player_1)

        elif x%2 != 0:
            y = 'O'
            player_2.append(number)
            print(player_2)
        b6.config(text=y)
        x=x+1

    if number == 7:
        if x%2 == 0:
            y = 'X'
            player_1.append(number)
            print(player_1)

        elif x%2 != 0:
            y = 'O'
            player_2.append(number)
            print(player_2)
        b7.config(text=y)
        x=x+1

    if number == 8:
        if x%2 == 0:
            y = 'X'
            player_1.append(number)
            print(player_1)

        elif x%2 != 0:
            y = 'O'
            player_2.append(number)
            print(player_2)
        b8.config(text=y)
        x=x+1

    if number == 9:
        if x%2 == 0:
            y = 'X'
            player_1.append(number)
            print(player_1)

        elif x%2 != 0:
            y = 'O'
            player_2.append(number)
            print(player_2)
        b9.config(text=y)
        x=x+1

    

root = Tk()

l1 = Label(root, text="Player 1 : X ", font='times 15')
l1.grid(row=0,column=0)

l2 = Label(root, text="Player 2 : O ", font='times 15')
l2.grid(row=0,column=1)

b1=Button(root, width=20, height=10, bg='pink', command=lambda: define_sign(1))
b1.grid(row=1, column=1)

b2=Button(root, width=20, height=10, bg='pink', command=lambda: define_sign(2))
b2.grid(row=1, column=2)

b3=Button(root, width=20, height=10, bg='pink', command=lambda: define_sign(3))
b3.grid(row=1, column=3)

b4=Button(root, width=20, height=10, bg='pink', command=lambda: define_sign(4))
b4.grid(row=2, column=1)

b5=Button(root, width=20, height=10, bg='pink', command=lambda: define_sign(5))
b5.grid(row=2, column=2)

b6=Button(root, width=20, height=10, bg='pink', command=lambda: define_sign(6))
b6.grid(row=2, column=3)

b7=Button(root, width=20, height=10, bg='pink', command=lambda: define_sign(7))
b7.grid(row=3, column=1)

b8=Button(root, width=20, height=10, bg='pink', command=lambda: define_sign(8))
b8.grid(row=3, column=2)

b9=Button(root, width=20, height=10, bg='pink', command=lambda: define_sign(9))
b9.grid(row=3, column=3)



root.mainloop()