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
canvas.grid(column=1, row=0)

# Website Entry
website_label = Label(text='Website:', bg='white', fg='black', font=('Ariel', 14), highlightthickness=0)
website_label.grid(column=0, row=1)
website_entry = Entry(bg='white', width=35, highlightthickness=0)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky=EW)

# Username Entry
username_label = Label(text='Email/Username:', bg='white', fg='black', font=('Ariel', 14), highlightthickness=0)
username_label.grid(column=0, row=2)
username_entry = Entry(bg='white', width=35, highlightthickness=0)
username_entry.grid(column=1, row=2, columnspan=2, sticky=EW)

# Password Entry
password_label = Label(text='Password:', bg='white', fg='black', font=('Ariel', 14), highlightthickness=0)
password_label.grid(column=0, row=3)
password_entry = Entry(bg='white', width=21, highlightthickness=0)
password_entry.grid(column=1, row=3, columnspan=1, sticky=EW)
generate_password_button = Button(text='Generate Password', bg='white', font=('Ariel', 14))
generate_password_button.grid(column=2, row=3)

# Add Button
add_button = Button(text='Add', bg='white', font=('Ariel', 15), width=36)
add_button.grid(column=1, row=4, columnspan=2, sticky=EW)






canvas.mainloop()
