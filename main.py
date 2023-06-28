from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    random_letters = [password_list.append(random.choice(letters)) for letter in range(nr_letters)]

    random_symbols = [password_list.append(random.choice(symbols)) for symbol in range(nr_symbols)]

    random_numbers = [password_list.append(random.choice(numbers)) for number in range(nr_numbers)]

    random.shuffle(password_list)

    password = ''.join(password_list)

    print(f"Your password is: {password}")

    password_entry.insert(0, f'{password}')

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0 or len(username_entry.get()) == 0:
        messagebox.showerror(message='Please Enter valid information')
    else:
        is_ok = messagebox.askokcancel(message=f'Is this correct?\n Website: {website_entry.get()}\n Email: {username_entry.get()}\n '
                                                                  f'Password: {password_entry.get()}')
        if is_ok:
            with open('data.txt', mode='a') as passwords:
                passwords.write(f'{website_entry.get()} | {username_entry.get()} | {password_entry.get()}\n')
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50,)

canvas = Canvas(width=200, height=200, highlightthickness=0)
myimg = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=myimg)
canvas.grid(column=1, row=0)

# Website Entry
website_label = Label(text='Website:', font=('Ariel', 14), highlightthickness=0)
website_label.grid(column=0, row=1)
website_entry = Entry(width=35, highlightthickness=0)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky=EW)

# Username Entry
username_label = Label(text='Email/Username:', font=('Ariel', 14), highlightthickness=0)
username_label.grid(column=0, row=2)
username_entry = Entry(width=35, highlightthickness=0)
username_entry.insert(0, 'jhines6092@gmail.com')
username_entry.grid(column=1, row=2, columnspan=2, sticky=EW)

# Password Entry
password_label = Label(text='Password:', font=('Ariel', 14), highlightthickness=0)
password_label.grid(column=0, row=3)
password_entry = Entry(width=21, highlightthickness=0)
password_entry.grid(column=1, row=3, columnspan=1, sticky=EW)
generate_password_button = Button(text='Generate Password', bg='white', font=('Ariel', 14), command=gen_password)
generate_password_button.grid(column=2, row=3)

# Add Button
add_button = Button(text='Add', font=('Ariel', 15), width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky=EW)

canvas.mainloop()
