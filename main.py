import tkinter as tk
from quiz import load_questions

TIME_LIMIT = 10

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("500x400")

        self.questions = load_questions()
        self.reset_quiz()

        self.question_label = tk.Label(root, text="", wraplength=450, font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.timer_label = tk.Label(root, text="", fg="red", font=("Arial", 12))
        self.timer_label.pack()

        self.var = tk.StringVar()

        self.options = []
        for _ in range(4):
            btn = tk.Radiobutton(root, text="", variable=self.var, font=("Arial", 12))
            btn.pack(anchor="w", padx=40)
            self.options.append(btn)

        self.feedback = tk.Label(root, text="", font=("Arial", 12))
        self.feedback.pack(pady=10)

        self.next_button = tk.Button(root, text="Next", command=self.next_question)
        self.next_button.pack(pady=5)

        self.restart_button = tk.Button(root, text="Restart", command=self.restart_quiz)
        self.restart_button.pack(pady=5)

        self.load_question()
        self.update_timer()

    def reset_quiz(self):
        self.q_index = 0
        self.score = 0
        self.time_left = TIME_LIMIT

    def load_question(self):
        self.var.set("")
        self.feedback.config(text="")
        self.time_left = TIME_LIMIT

        if self.q_index < len(self.questions):
            q = self.questions[self.q_index]
            self.question_label.config(text=q["question"])

            for i, option in enumerate(q["options"]):
                self.options[i].config(text=option, value=option)
        else:
            self.show_result()

    def next_question(self):
        selected = self.var.get()
        correct = self.questions[self.q_index]["answer"]

        if selected == correct:
            self.score += 1
            self.feedback.config(text="✅ Correct!", fg="green")
        else:
            self.feedback.config(text=f"❌ Correct Answer: {correct}", fg="red")

        self.root.after(800, self.move_next)

    def move_next(self):
        self.q_index += 1
        self.load_question()

    def update_timer(self):
        if self.q_index < len(self.questions):
            self.timer_label.config(text=f"⏳ Time Left: {self.time_left}s")

            if self.time_left > 0:
                self.time_left -= 1
                self.root.after(1000, self.update_timer)
            else:
                correct = self.questions[self.q_index]["answer"]
                self.feedback.config(text=f"⏰ Time’s Up! Answer: {correct}", fg="red")
                self.root.after(800, self.move_next)

    def show_result(self):
        percentage = (self.score / len(self.questions)) * 100
        self.question_label.config(
            text=f"🏁 Quiz Completed!\n\nScore: {self.score}/{len(self.questions)}\nPercentage: {percentage:.2f}%"
        )

        self.timer_label.config(text="")
        for btn in self.options:
            btn.pack_forget()
        self.next_button.pack_forget()

    def restart_quiz(self):
        self.reset_quiz()

        for btn in self.options:
            btn.pack(anchor="w", padx=40)

        self.next_button.pack(pady=5)
        self.feedback.config(text="")
        self.load_question()
        self.update_timer()


root = tk.Tk()
app = QuizApp(root)
root.mainloop()
