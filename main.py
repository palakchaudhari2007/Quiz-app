import tkinter as tk
from quiz import load_questions

TIME_LIMIT = 10

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("500x400")

        self.questions = load_questions()

        self.q_no = 0
        self.score = 0
        self.time_left = TIME_LIMIT

        # question text
        self.q_label = tk.Label(root, text="", wraplength=450, font=("Arial", 14))
        self.q_label.pack(pady=20)

        # timer
        self.timer = tk.Label(root, text="", fg="red")
        self.timer.pack()

        self.answer_var = tk.StringVar()

        # options
        self.option_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.answer_var, value="")
            rb.pack(anchor="w", padx=40)
            self.option_buttons.append(rb)

        # feedback
        self.feedback = tk.Label(root, text="")
        self.feedback.pack(pady=10)

        # next button
        self.next_btn = tk.Button(root, text="Next", command=self.next_question)
        self.next_btn.pack(pady=5)

        # restart button
        self.restart_btn = tk.Button(root, text="Restart Quiz", command=self.restart_quiz)
        self.restart_btn.pack()
        self.restart_btn.pack_forget()  # hide at start

        self.show_question()
        self.countdown()

    def show_question(self):
        self.answer_var.set("")
        self.feedback.config(text="")
        self.time_left = TIME_LIMIT

        if self.q_no < len(self.questions):
            q = self.questions[self.q_no]
            self.q_label.config(text=f"Q{self.q_no + 1}: {q['question']}")

            for i in range(4):
                self.option_buttons[i].config(
                    text=q["options"][i],
                    value=q["options"][i]
                )
        else:
            self.show_result()

    def next_question(self):
        selected = self.answer_var.get()
        correct_ans = self.questions[self.q_no]["answer"]

        if selected == correct_ans:
            self.score += 1
            self.feedback.config(text="Correct!", fg="green")
        else:
            self.feedback.config(text=f"Wrong! Ans: {correct_ans}", fg="red")

        self.root.after(700, self.move_ahead)

    def move_ahead(self):
        self.q_no += 1
        self.show_question()

    def countdown(self):
        if self.q_no < len(self.questions):
            self.timer.config(text=f"Time left: {self.time_left}s")

            if self.time_left > 0:
                self.time_left -= 1
                self.root.after(1000, self.countdown)
            else:
                correct_ans = self.questions[self.q_no]["answer"]
                self.feedback.config(text=f"Time up! Ans: {correct_ans}", fg="red")
                self.root.after(700, self.move_ahead)

    def show_result(self):
        percent = (self.score / len(self.questions)) * 100

        self.q_label.config(
            text=f"Quiz Finished!\n\nScore: {self.score}/{len(self.questions)}\nPercentage: {percent:.2f}%"
        )

        self.timer.config(text="")
        for rb in self.option_buttons:
            rb.pack_forget()

        self.next_btn.pack_forget()
        self.restart_btn.pack()

    def restart_quiz(self):
        self.q_no = 0
        self.score = 0

        for rb in self.option_buttons:
            rb.pack(anchor="w", padx=40)

        self.next_btn.pack(pady=5)
        self.restart_btn.pack_forget()

        self.show_question()
        self.countdown()


root = tk.Tk()
app = QuizApp(root)
root.mainloop()