from tkinter import *
from PIL import Image, ImageTk

# constants
CANVAS_W, CANVAS_H = 200, 200
WHITE = "#FFFFFF"


# save input data to a file

def save():
    with open("data.txt", "a") as f:
        f.write(website_textbox.get() + " | " + username_textbox.get() + " | " + password_textbox.get() + "\n")

    clear()

def clear():
    website_textbox.delete(0, END)
    username_textbox.delete(0, END)
    password_textbox.delete(0, END)

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
website_textbox.grid(row=2, column=1, columnspan=3, sticky="ew")

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
generate_password = Button(text="Generate password")
generate_password.grid(row=4, column=2, sticky="ew")

# add password to the list

add_pswd = Button(text="Add", command=save)
add_pswd.grid(row=5, column=1, columnspan=4, sticky="ew")

window.mainloop()
