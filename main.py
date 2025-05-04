# Write you random password generator program here!
import tkinter as tk

import string
import random
from tkinter import messagebox

#it makes a window with a comment on the top left hand corner
window = tk.Tk()
window.title("Password Generator")

#create text
tk.Label(window,text="Website:").pack()
website_entry = tk.Entry(window)
website_entry.pack(padx=20)

tk.Label(window,text="Login ID:").pack()
login_id_entry = tk.Entry(window)
login_id_entry.pack(padx=20)

numbers_var = tk.BooleanVar()
check_button = tk.Checkbutton(window,text="Include Numbers",variable=numbers_var)
check_button.pack()

uppercase_var = tk.BooleanVar()
tk.Checkbutton(window, text="Include Uppercase",variable=uppercase_var).pack(padx=20)

lowercase_var = tk.BooleanVar()
tk.Checkbutton(window, text="Include Lowercase",variable=lowercase_var).pack(padx=20)

special_char_var = tk.BooleanVar()
tk.Checkbutton(window, text="Include Special Characters",variable=special_char_var).pack(padx=20)

tk.Label(window, text="Password Length:").pack()
password_length_entry = tk.Entry(window)
password_length_entry.pack(pady=10)

def on_button_clicked():
    website = website_entry.get()
    login_id = login_id_entry.get()
    include_uppercase = uppercase_var.get()
    include_lowercase = lowercase_var.get()
    include_special_char = special_char_var.get()
    include_numbers = numbers_var.get()
    password_length = password_length_entry.get()

    gui_generate_password(website=website, login_id=login_id, include_uppercase=include_uppercase, include_lowercase=include_lowercase, include_special_char=include_special_char, include_numbers=include_numbers, password_length=password_length)


generate_button = tk.Button(window, text="Generate Password",command=on_button_clicked)
generate_button.pack()

def gui_generate_password(website, login_id,
                          include_uppercase, include_lowercase,
                          include_special_char, include_numbers,
                          password_length):
    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_special_char:
        characters += string.punctuation
    if include_numbers:
        characters += string.digits

    if not characters:
        messagebox.showerror("Error", "Please select at least one character type.")
        return

    try:
        password_length = int(password_length)
    except ValueError:
        messagebox.showerror("Error", "Password length must be a number.")
        return

    password = ''.join(random.choice(characters) for _ in range(password_length))

    # Write to file using .format() instead of f-string
    with open("passwords.txt", "a") as file:
        file.write(
            "Website: {site}, Login ID: {login}, Password: {pwd}\n"
            .format(site=website, login=login_id, pwd=password)
        )

    messagebox.showinfo("Generated Password", f"Your password: {password}")


window.mainloop()