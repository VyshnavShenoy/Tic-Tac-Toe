from tkinter import *
from tkinter import messagebox
import random


def button(frame):
    but = Button(frame, padx=1, text = " ", bd = 3, font=('noto sans', 26, 'bold'), fg='red', bg ='salmon', width=3, height=1, relief='sunken')
    return but


def turn():
    global a
    for i in ["O", "X"]:
        if not(i == a):
            a = i
            break


def check():
    for i in range(3):
        if game[i][0]["text"]==game[i][1]["text"]==game[i][2]["text"]==a or game[0][i]["text"]==game[1][i]["text"]==game[2][i]["text"]==a:
            messagebox.showinfo("Noice", f"{a} has won")
            reset()
    if game[0][0]["text"] == game[1][1]["text"] == game[2][2]["text"] == a or game[0][2]["text"] == game[1][1]["text"] == game[2][0]["text"] == a:
        messagebox.showinfo("Noice", f"{a} has won")
        reset()
    elif game[0][0]["state"]==game[0][1]["state"]==game[0][2]["state"]==game[1][0]["state"]==game[1][1]["state"]==game[1][2]["state"]==game[2][0]["state"]==game[2][1]["state"]==game[2][2]["state"]==DISABLED:
        messagebox.showinfo("Tied!!", "The match ended in a draw")
        reset()


def click(row, col):
    game[row][col].config(text=a, state=DISABLED)
    check()
    turn()
    label.config(text=a+"'s Move")


def comp():
    while True:
        i = random.randint(0, 2)
        j = random.randint(0, 2)
        if game[i][j]["state"] == NORMAL:
            game[i][j].config(text=a, state=DISABLED)
            check()
            turn()
            label.config(text=a+"'s Move")
            break


def reset():
    global a
    for i in range(3):
        for j in range(3):
            game[i][j]["text"] = " "
            game[i][j]["state"] = NORMAL
    a = "O"


root = Tk()
root.title("Tic-Tac-Toe")

a = "X"
game = [[], [], []]

label = Label(text=a+"'s Move", font=('railway dots', 25, 'bold'))
label.grid(row=3, column=0, columnspan=3)

for i in range(3):
    for j in range(3):
        game[i].append(button(root))
        game[i][j].config(command=lambda row=i, col=j: click(row, col))
        game[i][j].grid(row=i, column=j)



# label = Label(text=a+"'s Move",font=('arial',20,'bold'))
# label.grid(row=3,column=0,columnspan=3)
root.mainloop()
