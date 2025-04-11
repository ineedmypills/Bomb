import tkinter as tk

bomb = 100
score = 0
pressReturn = True
root = tk.Tk()
root.title("Кон Чен Ый")
root.geometry("600x680+500+500")
root.resizable(False, False)

enterLable = (tk.Label(
    root, text="Нажми [Enter] для начала игры",
    font=("Comic Sans MS", 15)
))
enterLable.pack()

fuseLabel = (tk.Label(root, text = f"Бомба: {str(bomb)}", font=("Comic Sans MS", 18)))
fuseLabel.pack()

scoreLabel = (tk.Label(root, text = f"Счёт: {str(score)}", font=("Comic Sans MS", 18)))
scoreLabel.pack()

normal_img = tk.PhotoImage(file="Images/normal.png")
bad_img = tk.PhotoImage(file="Images/bad.png")
tooBad_img = tk.PhotoImage(file="Images/tooBad.png")
end_img = tk.PhotoImage(file="Images/end.png")

bombLabel = tk.Label(root, image=normal_img)
bombLabel.pack()

def updateDisplay():
    global bomb, score
    if bomb >= 75:
        bombLabel.config(image=normal_img)
    elif 75 > bomb >= 50:
        bombLabel.config(image=bad_img)
    elif 50 > bomb >= 1:
        bombLabel.config(image=tooBad_img)
    else:
        bombLabel.config(image=end_img)

    fuseLabel.configure(text=f"Бомба: {str(bomb)}")
    scoreLabel.configure(text=f"Счёт: {str(score)}")
    fuseLabel.after(16, updateDisplay)

def isAlive():
    global bomb, pressReturn
    if bomb <=0:
        bomb = 0
        enterLable.config(text="БИЛЯЯЯЯЯЯЯЯЯЯЯ")
        pressReturn = True
        return False
    else:
        return True

def updateBomb():
    global bomb
    bomb -= 5
    if isAlive():
        fuseLabel.after(400, updateBomb)

def updateScore():
    global score
    if isAlive():
        score += 1
        scoreLabel.after(300, updateScore)

def start(event):
    global pressReturn
    if not pressReturn:
        return
    else:
        global bomb, score
        bomb = 100
        score = 0
        updateBomb()
        updateScore()
        updateDisplay()
        enterLable.config(text="")
        pressReturn = False


def click():
    global bomb
    if isAlive():
        bomb+=2
    else:
        return

clickButton = tk.Button(root, text="НАЖИМАЙ", bg="black", fg="white", width=15, font=("Comic Sans MS", 14), command=click)
clickButton.pack()

root.bind("<Return>", start)

root.mainloop()