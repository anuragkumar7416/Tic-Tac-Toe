from tkinter import*
from tkinter import messagebox

window = Tk()
window.title("TIC-TAC-TOE")

clicked = True
count = 0

# Reset Function for buttons
def reset():
    global count
    b1.config(text=" ", bg="cyan")
    b2.config(text=" ", bg="cyan")
    b3.config(text=" ", bg="cyan")
    b4.config(text=" ", bg="cyan")
    b5.config(text=" ", bg="cyan")
    b6.config(text=" ", bg="cyan")
    b7.config(text=" ", bg="cyan")
    b8.config(text=" ", bg="cyan")
    b9.config(text=" ", bg="cyan")
    count = 0



# Click function for button
def b_click(b):
    global clicked,count

    if b["text"] == " " and clicked == True:
        b["text"] ="X"
        clicked = False
        count += 1
        check_win()


    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_win()

    else:
        messagebox.showerror(" Hey! That box has already been selected")

# function for check who won
def check_win():

    global winner
    winner = False

# Check for X's wins
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"]== "X":
        b1.config(bg="yellow")
        b2.config(bg="yellow")
        b3.config(bg="yellow")
        winner = True
        messagebox.showinfo("TIC-TAC-TOE","Congrts!  X wins")
        reset()

    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="yellow")
        b5.config(bg="yellow")
        b6.config(bg="yellow")
        winner = True
        messagebox.showinfo("TIC-TAC-TOE", "Congrts!  X wins")
        reset()


    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="yellow")
        b8.config(bg="yellow")
        b9.config(bg="yellow")
        winner = True
        messagebox.showinfo("TIC-TAC-TOE", "Congrts!  X wins")
        reset()

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="yellow")
        b4.config(bg="yellow")
        b7.config(bg="yellow")
        winner = True
        messagebox.showinfo("TIC-TAC-TOE", "Congrts!  X wins")

    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="yellow")
        b5.config(bg="yellow")
        b8.config(bg="yellow")
        winner = True
        messagebox.showinfo("TIC-TAC-TOE", "Congrts!  X wins")
        reset()

    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="yellow")
        b6.config(bg="yellow")
        b9.config(bg="yellow")
        winner = True
        messagebox.showinfo("TIC-TAC-TOE", "Congrts!  X wins")
        reset()

    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="yellow")
        b5.config(bg="yellow")
        b9.config(bg="yellow")
        winner = True
        messagebox.showinfo("TIC-TAC-TOE", "Congrts!  X wins")
        reset()


    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="yellow")
        b5.config(bg="yellow")
        b7.config(bg="yellow")
        winner = True
        messagebox.showinfo("TIC-TAC-TOE", "Congrts!  X wins")
        reset()

# Check for O's wins
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="yellow")
        b2.config(bg="yellow")
        b3.config(bg="yellow")
        winner = True
        messagebox.showinfo("TIC-TAC-TOE", "Congrts!  O wins")
        reset()

    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="yellow")
        b5.config(bg="yellow")
        b6.config(bg="yellow")
        winner = True
        messagebox.showinfo("TIC-TAC-TOE", "Congrts!  O wins")
        reset()


    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="yellow")
        b8.config(bg="yellow")
        b9.config(bg="yellow")
        winner = True
        messagebox.showinfo("TIC-TAC-TOE", "Congrts!  O wins")
        reset()

    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="yellow")
        b4.config(bg="yellow")
        b7.config(bg="yellow")
        winner = True
        messagebox.showinfo("TIC-TAC-TOE", "Congrts!  O wins")

    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="yellow")
        b5.config(bg="yellow")
        b8.config(bg="yellow")
        messagebox.showinfo("TIC-TAC-TOE", "Congrts!  O wins")
        reset()

    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="yellow")
        b6.config(bg="yellow")
        b9.config(bg="yellow")
        winner = True
        messagebox.showinfo("TIC-TAC-TOE", "Congrts!  O wins")
        reset()

    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="yellow")
        b5.config(bg="yellow")
        b9.config(bg="yellow")
        winner = True
        messagebox.showinfo("TIC-TAC-TOE", "Congrts!  O wins")
        reset()


    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="yellow")
        b5.config(bg="yellow")
        b7.config(bg="yellow")
        winner = True
        messagebox.showinfo("TIC-TAC-TOE", "Congrts!  O wins")
        reset()

# Check for tie
    else:
        if count == 9 and winner == False:
            messagebox.showinfo("TIED","NO ONE WINS")
            reset()
# Buttons
b1 = Button(window,text=" ",font=("arial",48,"bold"),height=2,width=6,bg="cyan",command=lambda: b_click(b1) )
b2 = Button(window,text=" ",font=("arial",48,"bold"),height=2,width=6,bg="cyan",command=lambda: b_click(b2) )
b3 = Button(window,text=" ",font=("arial",48,"bold"),height=2,width=6,bg="cyan",command=lambda: b_click(b3) )
b4 = Button(window,text=" ",font=("arial",48,"bold"),height=2,width=6,bg="cyan",command=lambda: b_click(b4) )
b5= Button(window,text=" ",font=("arial",48,"bold"),height=2,width=6,bg="cyan",command=lambda: b_click(b5) )
b6 = Button(window,text=" ",font=("arial",48,"bold"),height=2,width=6,bg="cyan",command=lambda: b_click(b6) )
b7 = Button(window,text=" ",font=("arial",48,"bold"),height=2,width=6,bg="cyan",command=lambda: b_click(b7) )
b8 = Button(window,text=" ",font=("arial",48,"bold"),height=2,width=6,bg="cyan",command=lambda: b_click(b8) )
b9 = Button(window,text=" ",font=("arial",48,"bold"),height=2,width=6,bg="cyan",command=lambda: b_click(b9) )

# Grid for buttons

b1.grid(row=1,column=1)
b2.grid(row=1,column=2)
b3.grid(row=1,column=3)
b4.grid(row=2,column=1)
b5.grid(row=2,column=2)
b6.grid(row=2,column=3)
b7.grid(row=3,column=1)
b8.grid(row=3,column=2)
b9.grid(row=3,column=3)




window.mainloop()