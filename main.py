from tkinter import *
from random import *
from tkinter import messagebox

FONT = "SF Pro"
LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = '0123456789'
SYMBOLS = '!#$%&()*+'
ENTRY_WIDTH = 53
PASSWORD_WIDTH = 33


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    """
    Generates a random password containing letters, symbols, and numbers,
    and inserts it into the password entry widget.
    """
    password_entry.delete(0, END)
    password_list = [choice(LETTERS) for _ in range(randint(8, 10))]
    password_list += [choice(SYMBOLS) for _ in range(randint(2, 4))]
    password_list += [choice(NUMBERS) for _ in range(randint(2, 4))]
    shuffle(password_list)

    ai_pass = ''.join(password_list)
    password_entry.insert(0, ai_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """
    Save all user data into data.txt file and provide feedback.
    """
    website_data = website_entry.get()
    email = email_username_entry.get()
    password_data = password_entry.get()

    if len(website_data) == 0 or len(email) == 0 or len(password_data) == 0:
        messagebox.showwarning(title="Error", message="Please fill out all fields.")
    else:
        try:
            with open("data.txt", 'a') as data:
                data.write(f"{website_data} | {email} | {password_data}\n")
            website_entry.delete(0, END)
            email_username_entry.delete(0, END)
            password_entry.delete(0, END)
            messagebox.showinfo(title="Success", message="Password saved successfully.")
        except IOError:
            messagebox.showerror(title="Error", message="An error occurred while writing to the file.")

    # Set focus back to the website entry
    website_entry.focus()


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

website_entry = Entry(width=ENTRY_WIDTH)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")
website_entry.focus()  # Start with focus on this entry

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
generate_password = Button(text="Generate Password", highlightthickness=0, font=(FONT, 8, "bold"), command=generate_pass)
generate_password.grid(row=3, column=2, sticky="w")

# Add Button
add = Button(text="Add", highlightthickness=0, font=(FONT, 8, "bold"), command=save, width=45)
add.grid(row=4, column=1, columnspan=2, sticky="w")

window.mainloop()
