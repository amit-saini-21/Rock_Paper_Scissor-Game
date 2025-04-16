import tkinter as tk
import random 
from PIL import Image, ImageTk
from tkinter import messagebox 
import os

you = 0
comp = 0
images=["new new paper.png","new new rock.png","new new scissor"]
image_path = "images1.png"
image_path1 = "images1.png"

def click(s):
    global you, comp,image_path , image_path1, label, label1, result_label
    a = []
    l = ["rock", "paper", "scissor"]
    """ for i in range(5):
        b = random.choice(l)
        a.append(b)"""
    aa = random.choice(l)
    result = ""
    
    if s == "rock": 
        image_path = "new r download.png"
    elif s == "paper":
        image_path = "new pp download.png"
    else:
        image_path = "new ss download.png"
    
    if aa == "rock": 
       image_path1 ="new r download.png"
    elif aa == "paper":
      image_path1 = "new pp download.png"
    else:
       image_path1 = "new ss download.png"
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    label.config(image=photo, bg="#0B0C10")
    label.image = photo  # keep a reference to the image
    
    image1 = Image.open(image_path1)
    photo1 = ImageTk.PhotoImage(image1)
    label1.config(image=photo1, bg="#0B0C10")
    label1.image = photo1  # keep a reference to the image
    
    if s == aa:
        result = "Match Draw"
    elif (s == "rock" and aa == "scissor") or (s == "paper" and aa == "rock") or (s == "scissor" and aa == "paper"):
        result = "Congratulation You Won"
        you += 1
    else:
        result = "OOPS! You Lose"
        comp += 1

    # Update the result label text
    result_label.config(text=result)

    e1.delete(0, tk.END)
    e1.insert(tk.END, you)
    e2.delete(0, tk.END)
    e2.insert(tk.END, comp)

    if you == 10:
        messagebox.showinfo("End Result", "You Win The Match\n\nPress OK For Restart The Match")
        reset_game()
    elif comp == 10:
        messagebox.showinfo("End Result", "You Lose The Match\n\nPress OK for Restart The Match")
        reset_game()

def reset_game():
    global you, comp
    you = 0
    comp = 0
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    result_label.config(text="")

root = tk.Tk()
root.title("Rock-Paper-Scissor")
root.configure(bg="#0B0C10")

image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo, height=270, width=245, justify="center")
label.image = photo  # keep a reference to the image
label.place(x=70, y=285)

image1 = Image.open(image_path1)
photo1 = ImageTk.PhotoImage(image1)
label1 = tk.Label(root, image=photo1, height=270, width=245, justify="center")
label1.image = photo1  # keep a reference to the image
label1.place(x=550, y=285)

root.minsize(850, 650)
root.maxsize(850, 650)

l1 = tk.Label(root, text="Rock-Paper-Scissor", font=("algerian", 32, "bold"), bg="#0B0C10", fg="#66FCF1")
l1.place(x=200, y=20)

e1 = tk.Entry(root, bg="black", fg="White", font=("arial", 30, "bold"), justify="center", width=2)
e1.place(x=20, y=90)

e2 = tk.Entry(root, bg="black", fg="White", font=("arial", 30, "bold"), justify="center", width=2)
e2.place(x=780, y=90)

l1 = tk.Label(root, text="YOU", font=("algerian", 20, "bold"), fg="red", bg="#0B0C10")
l1.place(x=80, y=100)

l2 = tk.Label(root, text="COMPUTER", font=("algerian", 20, "bold"), fg="red", bg="#0B0C10")
l2.place(x=612, y=100)

# Styling for the buttons
button_style = {
    "activebackground": "#45A29E",
    "activeforeground": "White",
    "background": "#1F2833",
    "fg": "White",
    "font": ("Algerian", 18, "bold"),
    "height": 3,
    "width": 10,
    "relief": tk.GROOVE,
    "bd": 2,
}
'''rock_path="new new rock.png"
rock_image=Image.open(rock_path)
rock_photo=ImageTk.PhotoImage(rock_image)'''
b1 = tk.Button(root,text="ROCK", command=lambda: click("rock"),**button_style)
b1.place(x=80, y=160)
'''paper_path="new new paper.png"
paper_image=Image.open(paper_path)
paper_photo=ImageTk.PhotoImage(paper_image)'''
b2 = tk.Button(root, text="PAPER", command=lambda: click("paper"),**button_style)
b2.place(x=350, y=160)
'''scissor_path="new new scissor.png"
scissor_image=Image.open(scissor_path)
scissor_photo=ImageTk.PhotoImage(scissor_image)'''
b3 = tk.Button(root,text="SCISSOR", command=lambda: click("scissor"),**button_style)
b3.place(x=600, y=160)

# Result label instead of entry
result_label = tk.Label(root, bg="#0B0C10", fg="yellow", font=("Algerian", 24, "bold"), justify="center", width=37)
result_label.place(x=50, y=570)

root.mainloop()





