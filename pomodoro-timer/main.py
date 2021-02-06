from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WHITE = "#ffffff"
BLACK = "#000000"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
marks = ""
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps
    reps = 0
    global marks
    marks = ""
    window.after_cancel(timer)
    timer_label.config(text="Timer", bg=YELLOW, fg=GREEN)
    canvas.config(bg=YELLOW)
    window.config(bg=YELLOW)
    check_label.config(bg=YELLOW, text=marks)
    canvas.itemconfig(timer_text, text="00:00")
    start_button["state"] = "active"
    reset_button["state"] = "disabled"
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    work_sec = 5 #WORK_MIN * 60
    short_break_sec = 5 #SHORT_BREAK_MIN * 60
    long_break_sec = 5 #LONG_BREAK_MIN * 60
    start_button["state"] = "disabled"
    reset_button["state"] = "active"

    if reps % 2 == 1 and reps < 8:
        count_down(work_sec) #green
        timer_label.config(text="Work", bg=GREEN, fg=YELLOW)
        canvas.config(bg=GREEN)
        window.config(bg=GREEN)
        check_label.config(bg=GREEN)

    elif reps == 8:
        count_down(long_break_sec) #red
        timer_label.config(text="Break", bg=RED, fg=YELLOW)
        canvas.config(bg=RED)
        window.config(bg=RED)
        check_label.config(bg=RED)

    elif reps % 2 == 0 and reps < 8:
        count_down(short_break_sec) #pink
        timer_label.config(text="Break", bg=PINK, fg=YELLOW)
        canvas.config(bg=PINK)
        window.config(bg=PINK)
        check_label.config(bg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):

    count_min = math.floor(count / 60)
    count_seconds = count % 60

    if count_seconds < 10:
        print("part 1")
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_seconds}")
    if count > 0:
        print("part 2")
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        print("part 3")
        start_timer()
        global marks
        marks = ""
        work_sessions = math.floor(reps/2)
        print(work_sessions)
        for _ in range(work_sessions):
            marks += "✓"
        check_label.config(text=marks, fg=YELLOW)

    # ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 16, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, "bold"))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", bg=WHITE, fg=BLACK, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg=WHITE, fg=BLACK, command=reset_timer)
reset_button.grid(column=2, row=2)
reset_button["state"] = "disabled"

check_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, "bold"))
check_label.grid(column=1, row=3)

window.mainloop()
