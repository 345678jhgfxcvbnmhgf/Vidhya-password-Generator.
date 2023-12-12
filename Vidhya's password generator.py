from tkinter import *
import random
root = Tk()
root.geometry("700x500")
passwrd = StringVar()
passlen = IntVar()
passlen.set(0)
def generate(): 
	pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
			'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
			'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
			'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
			'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
			'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
			'9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
			'*', '(', ')']
	password = ""
	for x in range(passlen.get()):
		password = password + random.choice(pass1)
	passwrd.set(password)
def copyclipboard():
	random_password = passwrd.get()
	pyperclip.copy(random_password)
Label(root, text="Vidhya's Strong Password Generator", font="Courier 30 bold").pack()
Label(root, text="Crock Star", font="Courier 20 italic").pack()
Label(root, text="Enter the length of the password").pack(pady=3)
Entry(root, textvariable=passlen).pack(pady=3)
Button(root, text="Generate a password of the specified length", command=generate).pack(pady=7)
Entry(root, textvariable=passwrd).pack(pady=3)
Button(root, text="Print the generated password on the screen", command=copyclipboard).pack()
root.mainloop()
