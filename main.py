from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20, bg='white')

canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
myimg = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=myimg)
canvas.grid(column=0, row=0)








canvas.mainloop()
