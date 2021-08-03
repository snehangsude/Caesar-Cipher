from tkinter import *
from model import Cipher

THEME = "#444444"


class CipherInterface:
    """class contains methods to launch the Caesar GUI"""

    def __init__(self):
        """
        Initializes the interface of the application
        """

        self.cipher = Cipher()
        self.window = Tk()
        self.window.title('Caesar Cipher')
        self.window.config(bg=THEME, padx=50, pady=50)

        # Helps reset the spinbox to zero
        self.var = IntVar(self.window)

        # Initializing the note on top
        self.note = Label(text="Type the text you'd like to convert", font=("Bookman Old Style", 15, "bold underline"),
                          bg=THEME, fg='#B2B1B9', )
        self.note.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

        # Initializing Input Text space
        self.input = Text(width=30, height=3, font=("Bookman Old Style", 15, "bold"), bg=THEME,
                          fg='grey70', wrap='word', )
        self.input.focus()
        self.input.grid(row=2, column=1, columnspan=3, padx=10, pady=10)

        # Initializing choices as buttons
        self.decrypt = Button(bd=-2, highlightthickness=0, text='Decrypt', bg=THEME, padx=2, pady=2,
                              font=("Tahoma", 17, "bold"), fg="#D79771", command=self.decrypt_msg)
        self.decrypt.grid(row=3, column=3, rowspan=2)

        self.encrypt = Button(bd=-2, highlightthickness=0, text='Encrypt', bg=THEME, padx=2, pady=2,
                              font=("Tahoma", 17, "bold"), fg="#71EFA3", command=self.encrypt_msg)
        self.encrypt.grid(row=3, column=1, rowspan=2)

        # Initializing Spinbox
        self.spinbox = Spinbox(from_=0, to=10000, width=8, command=self.spinbox_used, bg=THEME, fg='grey70',
                               font=("Tahoma", 11, 'bold'), justify='center')
        self.spinbox.grid(row=3, column=2, rowspan=2)

        # Initializing Result space
        self.result = Text(width=30, height=3, font=("Tahoma", 15, "bold"), bg=THEME, fg='grey70', wrap='word', )
        self.result.grid(row=5, column=1, columnspan=3, padx=10, pady=10)

        # Initializing the Clear button
        self.clear = Button(bd=-2, width=26, highlightthickness=0, text='Clear', bg=THEME, padx=2, pady=2,
                            font=("Tahoma", 17, "bold"), fg="#FDE49C", command=self.delete)
        self.clear.grid(row=6, column=1, columnspan=3)

        self.window.mainloop()

    def spinbox_used(self):
        """Function to get the value in the spinbox"""
        return int(self.spinbox.get())

    def encrypt_msg(self):
        """Function bind with the Encrypt button in the GUI to encrypt the text"""
        text1 = self.input.get("1.0", END).lower()
        move1 = self.spinbox_used()
        self.spinbox.config(textvariable=self.var)
        self.reset()
        message = self.cipher.encrypt(text1, move1)
        self.note.config(text="Please clear box after each output")
        self.result.insert(END, message)

    def decrypt_msg(self):
        """Function bind with the Decrypt button in the GUI to decrypt the text"""
        text = self.input.get("1.0", END).lower()
        move = self.spinbox_used()
        self.spinbox.config(textvariable=self.var)
        self.reset()
        answer = self.cipher.decrypt(text, move)
        self.note.config(text="Please clear box after each output")
        self.result.insert(END, answer)

    def delete(self):
        """Clears the output box"""
        self.result.delete(1.0, END)
        self.note.config(text="Type the text you'd like to convert")

    def reset(self):
        """Resets the value in the spinbox after each click"""
        self.var.set(0)
