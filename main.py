import json
import os
from tkinter import *
from random import choice, randint, shuffle
from tkinter import messagebox
import pyperclip

FONT = "SF Pro"
LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = '0123456789'
SYMBOLS = '!#$%&()*+'
ENTRY_WIDTH = 53
PASSWORD_WIDTH = 32
SEARCH_WIDTH = 16
ADD_WIDTH = 45
DATA_FILE = "data.json"


# ---------------------------- HELPER FUNCTIONS ------------------------------- #
def read_data():
    """
    Read password data from a JSON file. If the file doesn't exist, return an empty dictionary.
    """
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as data_file:
                return json.load(data_file)
        except (json.JSONDecodeError, FileNotFoundError):
            return {}
    return {}


def write_data(data):
    """
    Write the given data to a JSON file.
    """
    with open(DATA_FILE, 'w') as data_file:
        json.dump(data, data_file, indent=4)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    """
    Generate a random password containing letters, symbols, and numbers.
    """
    password_entry.delete(0, END)
    password_list = [choice(LETTERS) for _ in range(randint(8, 10))]
    password_list += [choice(SYMBOLS) for _ in range(randint(2, 4))]
    password_list += [choice(NUMBERS) for _ in range(randint(2, 4))]
    shuffle(password_list)

    ai_pass = ''.join(password_list)
    password_entry.insert(0, ai_pass)
    pyperclip.copy(ai_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """
    Save the entered website, email, and password data to a JSON file.
    """
    website_data = website_entry.get().capitalize().strip()
    email = email_username_entry.get().lower().strip()
    password_data = password_entry.get()

    if not website_data or not email or not password_data:
        messagebox.showwarning(title="Error", message="Please fill out all fields.")
        return

    new_data = {
        website_data: {
            "email": email,
            "password": password_data
        }
    }

    try:
        data = read_data()
        data.update(new_data)
        write_data(data)
        messagebox.showinfo(title="Success", message="Password saved successfully.")
    except Exception as e:
        messagebox.showerror(title="Error", message=f"An error occurred: {e}")
    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()


# ---------------------------- SEARCH ------------------------------- #
def search_fun():
    """
    Search for a website's email and password in the JSON file.
    """
    website_data = website_entry.get().capitalize().strip()
    if not website_data:
        messagebox.showwarning(title="Error", message="Please enter a website name to search.")
        return

    try:
        data = read_data()
        if website_data in data:
            email = data[website_data]["email"]
            password_data = data[website_data]["password"]
            messagebox.showinfo(title=website_data, message=f"Email: {email}\nPassword: {password_data}")
        else:
            messagebox.showerror(title="Error", message=f"No details for {website_data} found.")
    except Exception as e:
        messagebox.showerror(title="Error", message=f"An error occurred: {e}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Website Label and Entry
website = Label(text="Website:", font=(FONT, 8, "bold"))
website.grid(row=1, column=0)

website_entry = Entry(width=PASSWORD_WIDTH)
website_entry.grid(row=1, column=1, sticky="w")
website_entry.focus()

# Search button
search = Button(text="Search", highlightthickness=0, font=(FONT, 8, "bold"), command=search_fun, width=SEARCH_WIDTH)
search.grid(row=1, column=2, sticky="w")

# Email Label and Entry
email_username = Label(text="Email/Username:", font=(FONT, 8, "bold"))
email_username.grid(row=2, column=0)

email_username_entry = Entry(width=ENTRY_WIDTH)
email_username_entry.grid(row=2, column=1, columnspan=2, sticky="w")
email_username_entry.insert(0, "default@xmail.com")

# Password Label and Entry
password = Label(text="Password:", font=(FONT, 8, "bold"))
password.grid(row=3, column=0)

password_entry = Entry(width=PASSWORD_WIDTH)
password_entry.grid(row=3, column=1, sticky="w")

# Generate Password Button
generate_password = Button(text="Generate Password", highlightthickness=0, font=(FONT, 8, "bold"),
                           command=generate_pass, width=SEARCH_WIDTH)
generate_password.grid(row=3, column=2, sticky="w")

# Add Button
add = Button(text="Add", highlightthickness=0, font=(FONT, 8, "bold"), command=save, width=ADD_WIDTH)
add.grid(row=4, column=1, columnspan=2, sticky="w")

window.mainloop()
