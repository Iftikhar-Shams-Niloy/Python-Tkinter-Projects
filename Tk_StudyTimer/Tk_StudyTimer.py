import tkinter
import random

tracker = None
total_studied = None
switch = False

def reset():
    global switch
    title_lable.config(text="Study-Timer")
    canvas.itemconfig(timer_text,text="00\n00")
    window.after_cancel(tracker)
    status.config(text='💤😴💤')
    switch = False
def start():
    global switch
    if switch == False:
        title_lable.config(text=random.choice(study_quotes))
        count_down(30*60)
        switch = True

def count_down(count):
    global tracker
    global total_studied
    def studying_text(count):
        if count%3==2:
            status.config(text='Studing.')
        elif count%3 == 1:
            status.config(text='Studing..')
        elif count%3 == 0:
            status.config(text='Studing...')
    def send_total(tracker):
        temp = tracker.split('#')
        total = int(temp[1])
        final_time = str(total//60)+" Minutes " + str(total%60)+" Seconds"
        return final_time
    minute = count//60
    second = (count-minute*60)%60
    if minute < 10:
        minute = "0"+str(minute)
    if second < 10:
        second = "0"+str(second)
    final_text= str(minute)+"\n"+str(second)
    if count >= 0:
        studying_text(count)
        canvas.itemconfig(timer_text, text=final_text)
        tracker = window.after(1000, count_down, count-1)
        total_studied = send_total(tracker)

def show_total():
    global total_studied
    total_out.config(text= total_studied)

my_font1 = ('Helvetica',20, "bold")
my_font2 = ('Brush Script Std', 25, "normal")
my_font3 = ('Brush Script Std', 17, "normal")
bg_list = ['steelblue1','steelblue2','steelblue3']
study_quotes= [
    '"End is not the end if \nfact E.N.D. Means \n"Efforts Never Dies".\n – Dr. A.P.J. Abdul Kalam',
    '"Education is the most \npowerful weapon you can \nuse to change the world."\n – Nelson Mandela',
    '"A person who never made \na mistake never tried anything new."\n – Albert Einstein',
    '"There are plenty of difficult \nobstacles in your path. \nDont allow yourself to \nbecome one of them."\n – Ralph Marston',
    '"Only I can change my life. \nNo one can do it for me."\n – Carol Burnett',
    '"I think I can. \nI know I can."\n – Jennifer Wittwer',
    '"Learning is never done \nwithout error, and defeat "\n – Vladimir Lenin',
    '"There is no substitute \nfor hard work."\n – Thomas Alva Edison',
    '"Dont wait for \nthe opportunity. Create it."\n – George Bernard Shaw']


pick_bg = random.choice(bg_list)
window = tkinter.Tk()
window.title("StudyTimer")
window.config(padx=10,pady=10, bg=pick_bg)

title_lable = tkinter.Label(text="Study-Timer", fg='RoyalBlue4',bg=pick_bg , font=my_font2, highlightthickness=0)
title_lable.grid(column=1, row=0)

canvas = tkinter.Canvas(width=200, height=200, bg=pick_bg, highlightthickness=0)
pick_image = tkinter.PhotoImage(file='deer.png')
clock_image = canvas.create_image(100,100, image= pick_image)
timer_text = canvas.create_text(100,68, text='00\n00', font=my_font1, fill='black')
canvas.grid(column=1, row=2)

start_button = tkinter.Button(text="Start", font=my_font3, fg = 'RoyalBlue4', bg = pick_bg
                              , highlightthickness=0, relief='ridge', activebackground = 'forest green',
                              command = start)
start_button.grid(column=0, row=3)

reset_button = tkinter.Button(text="Reset", font=my_font3, fg = 'RoyalBlue4', bg = pick_bg
                              , highlightthickness=0,activebackground = 'firebrick3', relief='ridge'
                              , command=reset)
reset_button.grid(column=2, row=3)

status = tkinter.Label(text="✅", fg='midnight blue', bg=pick_bg, font=my_font2,pady=10)
status.grid(column=1, row=3)

total_button = tkinter.Button(text="Total Studied", font=my_font3, fg = 'RoyalBlue4', bg = pick_bg
                              , highlightthickness=0, relief='ridge', activebackground = 'blue'
                              , command = show_total)
total_button.grid(column=1, row=4)

total_out = tkinter.Label(text="0 Minutes 0 Seconds", font=my_font2, fg = 'dark slate blue', bg = pick_bg
                              , highlightthickness=0, pady=5)
total_out.grid(column=1, row=6)

window.mainloop()
