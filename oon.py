import tkinter as tk
import time

# ----------------------------
# Quiz Data
# ----------------------------
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which language is used to write Python programs?",
        "options": ["Java", "Python", "C++", "HTML"],
        "answer": "Python"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "Central Process Unit",
            "Computer Personal Unit",
            "Central Processing Unit",
            "Control Processing Unit"
        ],
        "answer": "Central Processing Unit"
    }
]

# ----------------------------
# Global Variables
# ----------------------------
current_question = 0
score = 0
start_time = 0
TIME_LIMIT = 10  # seconds

# ----------------------------
# Functions
# ----------------------------
def load_question():
    global start_time

    start_time = time.time()
    q = questions[current_question]
    question_label.config(text=q["question"])
    result_label.config(text="")
    for i in range(4):
        
        option_buttons[i].config(text= q["options"][i], bg=["#441fff","#ff1f1f","#1f1fff","#ff1f2a"][i],state="normal")


def check_answer(selected_option):
    global current_question, score

    time_taken = time.time() - start_time

    if time_taken > TIME_LIMIT:
        result_label.config(text="Time's up!", fg="red",font=('Arial',30,'bold'))
    elif selected_option == questions[current_question]["answer"]:
        score += 1
        result_label.config(text="Correct!", fg="green")
    else:
        result_label.config(text="Wrong!", fg="red")

    for btn in option_buttons:
        btn.config(state="disable")

    window.after(1000, next_question)


def next_question():
    global current_question

    current_question += 1

    if current_question < len(questions):
        load_question()
    else:
        show_result()


def show_result():
    percentage = (score / len(questions)) * 100

    if percentage >= 80:
        grade = "A"
    elif percentage >= 50:
        grade = "B"
    else:
        grade = "C"

    question_label.config(text="Quiz Finished!")
    result_label.config(
        text=f"Score: {score}/{len(questions)}\n"
                f"Percentage: {int(percentage)}%\n"
                f"Grade: {grade}",
        fg="blue"
    )

    for btn in option_buttons:
        btn.pack_forget()


# ----------------------------
# GUI Setup
# ----------------------------
window = tk.Tk()
window.title("Quiz Game")
window.geometry("500x350")

question_label = tk.Label(
    window,
    text=" ",
    font=("Arial", 14,'bold'),
        wraplength=450
        
    
)
question_label.pack(pady=20)

option_buttons = []
for option in range(4):
    btn = tk.Button(
        window,
        text="",
        width=50,
        command=lambda opt=option: check_answer(
            questions[current_question]["options"][opt]
        )
    )
    btn.pack(pady=5)
    option_buttons.append(btn)

result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=20)

# Start quiz

if __name__== '__main__':
    load_question()
    
    
window.mainloop()
