from tkinter import *

BG = "#1a1a2e"
ACCENT = "#e94560"
TEXT = "#eaeaea"
ENTRY_BG = "#16213e"

window = Tk()
window.title("Miles → KM Converter")
window.config(bg=BG)
window.minsize(width=420, height=280)
window.resizable(False, False)

frame = Frame(window, bg=BG)
frame.pack(expand=True)

title = Label(frame, text="MILES → KM", font=("Arial", 26, "bold"), bg=BG, fg=ACCENT)
title.grid(row=0, column=0, columnspan=3, pady=(30, 24))

miles_label = Label(frame, text="Miles:", font=("Arial", 13), bg=BG, fg=TEXT)
miles_label.grid(row=1, column=0, padx=(30, 8))

entry = Entry(frame, width=10, font=("Arial", 13), bg=ENTRY_BG, fg=TEXT,
              insertbackground=TEXT, relief="flat", bd=8)
entry.grid(row=1, column=1)
entry.focus()

equals_label = Label(frame, text="=", font=("Arial", 13), bg=BG, fg=TEXT)
equals_label.grid(row=1, column=2, padx=(8, 30))

result_label = Label(frame, text="", font=("Arial", 22, "bold"), bg=BG, fg=TEXT)
result_label.grid(row=2, column=0, columnspan=3, pady=(18, 0))

button = Button(frame, text="CONVERT", font=("Arial", 13, "bold"),
                bg=ACCENT, fg="white", activebackground="#c73652",
                activeforeground="white", relief="flat",
                padx=24, pady=8, cursor="hand2", command=lambda: convert())
button.grid(row=3, column=0, columnspan=3, pady=(20, 30))


def convert():
    try:
        miles = float(entry.get())
        kilos = miles * 1.60934
        result_label.config(text=f"{kilos:.2f} km", fg=TEXT)
    except ValueError:
        result_label.config(text="Enter a valid number", fg=ACCENT)


window.bind("<Return>", lambda event: convert())

window.mainloop()