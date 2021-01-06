from tkinter import*
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(time_text,text="00:00")
    head_label.config(text="TIMER")
    checkmark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN 
    short_break_sec = SHORT_BREAK_MIN 
    long_break_sec = LONG_BREAK_MIN 
    #if its a 1,3,5,7 reps
    
    # if its the 8th reps 
    
    if reps % 2 ==0:
        if reps ==8:
            count_down(long_break_sec)
            head_label.config(text="LONG-BREAK" ,fg="RED", font=(FONT_NAME,25,"bold"),bg="#cae4db", highlightthickness=0)
            
        else:
            count_down(short_break_sec)
            head_label.config(text="SHORT-BREAK" ,fg="PINK", font=(FONT_NAME,25,"bold"),bg="#cae4db", highlightthickness=0)
            

    else:
        count_down(work_sec)
        head_label.config(text="TIMER" ,fg=GREEN)
    


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(time_text,text=f"{count_min}:{count_sec}")
    if count >0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps/2) #-----------for every 2 reps 1 work session complete
        for _ in range(work_session):
            mark +="✔"
        checkmark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.iconbitmap("title_icon.ico")
window.config(padx=100,pady=50, bg='#cae4db')

canvas = Canvas(width=205,height=240,bg="#cae4db", highlightthickness=0)
tomato_image=PhotoImage(file="tomato.png")
canvas.create_image(103,120,image=tomato_image)
time_text = canvas.create_text(103,140, text="00:00" , fill = "black" , font=(FONT_NAME,30,"bold"))
canvas.grid(column=1,row=1)



head_label = Label(text="TIMER" ,fg=GREEN, font=(FONT_NAME,60,"bold"),bg="#cae4db", highlightthickness=0)
head_label.grid(column=1,row=0)

start = Button(text="Start" ,command = start_timer)
start.grid(column=0,row=3)

reset = Button(text="Reset",command=reset_timer)
reset.grid(column=2,row=3)

checkmark = Label(text="",fg="#c70039",bg="#cae4db", highlightthickness=0, font=(50))
checkmark.grid(column=1,row=4)






window.mainloop()