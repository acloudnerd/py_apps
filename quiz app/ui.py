from tkinter import *
from tkinter import messagebox
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
CANVAS_HEIGHT = 250
CANVAS_WIDTH = 300
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20)
        self.window.configure(bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            CANVAS_WIDTH / 2,
            CANVAS_HEIGHT / 2,
            width=CANVAS_WIDTH - 40,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=FONT,
            justify="center",
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        right_image = PhotoImage(file="images/true.png")
        self.right = Button(image=right_image, highlightthickness=0)
        self.right.grid(row=2, column=0)

        wrong_image = PhotoImage(file="images/false.png")
        self.wrong = Button(image=wrong_image, highlightthickness=0)
        self.wrong.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text = q_text)
