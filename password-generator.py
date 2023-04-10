from tkinter import *
import random

window = Tk()

window.title("Testing Random Function")
window.geometry("500x500")

array_3D = [[["I","J","K","L","M","N","O","P"],["King","Queen"],["!","£","@","$","%","&","*"]]]

element = Entry(window)

guessed_password_label = Label(window)
generated_password = Label(window)

def new_password():
    guessed_password_label["text"] = "Guessed Password: " +element.get()
    r1 = random.randint(0,7)
    r2 = random.randint(0,1)
    r3 = random.randint(0,6)
    generated_password["text"] = "Generated Password : "+array_3D[0][0][r1]+array_3D[0][1][r2]+array_3D[0][2][r3]


btn = Button(window,text="New Password",command=new_password)


element.place(relx=0.5,rely=0.2,anchor=CENTER)
guessed_password_label.place(relx=0.5,rely=0.3,anchor=CENTER)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)
generated_password.place(relx=0.5,rely=0.5,anchor=CENTER)

window.mainloop()