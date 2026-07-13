from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import random
import pyperclip
import json

# constants
CANVAS_W, CANVAS_H = 200, 200
WHITE = "#FFFFFF"

# random password generator

def pswd_generator():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # build the password parts using list comprehensions
    password_list = [random.choice(letters) for _ in range(nr_letters)] \
        + [random.choice(symbols) for _ in range(nr_symbols)] \
        + [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    # join the characters into the final password string
    password = "".join(password_list)
    password_textbox.insert(0, password)
    pyperclip.copy(password)

    # print(f"Your password is: {password}")



# save input data to a file

def save():
    website = website_textbox.get()
    username = username_textbox.get()
    password = password_textbox.get()

    if not validations(website, username, password):
        return

    is_okay = messagebox.askokcancel(
        title=website,
        message=f"These are the details entered:\nUsername: {username}\nPassword: {password}\nIs it okay to save?"
    )

    if is_okay:
        new_data = {
            website: {
                "email": username,
                "password": password,
            }
        }

        try:
            with open("data.json", "r", encoding="utf-8") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        data.update(new_data)

        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        clear()


# clear the fields
def clear():
    website_textbox.delete(0, END)
    username_textbox.delete(0, END)
    password_textbox.delete(0, END)

# validations

def validations(website, username, password):
    if not website or not username or not password:
        messagebox.showerror(
            title="Do not allow empty fields",
            message="Please do not leave any fields empty"
        )
        return False
    return True

def search():
    search_text = website_textbox.get()
    try:
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showinfo(title="Error", message="Data file not found")
    else:
        if search_text in data:
            email = data[search_text]["email"]
            password = data[search_text]["password"]
            messagebox.showinfo(title=search_text, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Not Found", message=f"No details for {search_text} in your records")
    

# creating the window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.resizable(False, False)

# setting up and showing the canvas
canvas = Canvas(width=CANVAS_W, height=CANVAS_H)

pil_image = Image.open("logo.png").resize((CANVAS_W, CANVAS_H)).convert("RGBA")
background = Image.new("RGBA", (CANVAS_W, CANVAS_H), WHITE)
background.paste(pil_image, mask=pil_image.split()[3])
logo_img = ImageTk.PhotoImage(background.convert("RGB"))
canvas.create_image(CANVAS_W // 2, CANVAS_H // 2, image=logo_img)
canvas.grid(row=0, column=1, columnspan=3, sticky="ew")

# website
website_label = Label(window, text="Website:")
website_label.grid(row=2, column=0)
website_textbox = Entry(window)
website_textbox.focus()
website_textbox.grid(row=2, column=1, sticky="ew")

# email
username_label = Label(window, text="Username/Email:")
username_label.grid(row=3, column=0)
username_textbox = Entry(window)
username_textbox.insert(0, "tshepo@gmail.com")
username_textbox.grid(row=3, column=1, columnspan=3, sticky="ew")

# password
password_label = Label(window, text="Password:")
password_label.grid(row=4, column=0)
password_textbox = Entry(window, show="*")
password_textbox.grid(row=4, column=1)

# generate password button
generate_password = Button(text="Generate password", command=pswd_generator)
generate_password.grid(row=4, column=2, sticky="ew")

# add password to the list
add_pswd = Button(text="Add", command=save)
add_pswd.grid(row=5, column=1, columnspan=4, sticky="ew")

# search button
search = Button(text="Search", command=search)
search.grid(row=2, column=2, sticky="ew")

window.mainloop()
