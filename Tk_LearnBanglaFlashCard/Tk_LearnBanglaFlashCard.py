import tkinter
import random
import pandas

class EmptyError(Exception):
    "The Dataset is Empty!!!"
    pass

preset1 = {'background':'light cyan', 'textColor':'SteelBlue4', 'flashCard':'images/FlashCard1.png','flashCardFlipped':'images/FlashCard1_flipped.png'}
preset2 = {'background':'light coral', 'textColor':'IndianRed4', 'flashCard':'images/FlashCard2.png', 'flashCardFlipped':'images/FlashCard2_flipped.png'}
preset3 = {'background':'light goldenrod', 'textColor':'lightGoldenrod4', 'flashCard':'images/FlashCard3.png', 'flashCardFlipped':'images/FlashCard3_flipped.png'}
presets = [preset1, preset2, preset3]
myPreset = random.choice(presets)

myFont1 = ("Ariel", 30, "italic")
myFont2 = ("Ariel", 25, "normal")

try:
    data = pandas.read_csv('dataset/leftToLearn')
    data_dict = data.to_dict(orient='records')
    if len(data_dict) < 1:
        raise EmptyError
except EmptyError:
    data = pandas.read_csv('dataset/WordBank.csv')
    data_dict = data.to_dict(orient='records')
except FileNotFoundError:
    data = pandas.read_csv('dataset/WordBank.csv')
    data_dict = data.to_dict(orient='records')

def nextCard():
    if len(data_dict) >= 1:
        global picked_card
        global timer
        window.after_cancel(timer)
        picked_card = random.choice(data_dict)
        canvas.itemconfig(flashcardTitle, text='Bangla')
        show_text = f"{picked_card['Bangla']}({picked_card['Transliteration']})"
        canvas.itemconfig(flashcardWord, text=show_text)
        canvas.itemconfig(flashcardImage,image=card_front)
        timer = window.after(3000,func=flipCard)
    else:
        isAll()

def flipCard():
    canvas.itemconfig(flashcardTitle, text="English")
    canvas.itemconfig(flashcardWord, text=picked_card['Translation'])
    canvas.itemconfig(flashcardImage, image=card_back)

def isLearned():
    data_dict.remove(picked_card)
    save_data = pandas.DataFrame(data_dict)
    save_data.to_csv('dataset/leftToLearn')
    nextCard()

def isAll():
    global timer
    canvas.itemconfig(flashcardTitle, text="CONGRATULATIONS!", font=("Ariel", 25, "bold"))
    canvas.itemconfig(flashcardWord, text=" YOU HAVE LEARNED \nALL THE BASIC WORDS\n     OF BANGLA!", font=("Ariel", 20, "italic"))
    canvas.itemconfig(flashcardImage, image=card_front)
    right_button.destroy()
    wrong_button.destroy()
    window.after_cancel(timer)

window = tkinter.Tk()
window.title("Learn-Bangla FLASHCARD")
window.config(padx=50, pady=25, bg= myPreset['background'])

timer = window.after(3000, func=flipCard)

canvas = tkinter.Canvas(width=400, height=400)
card_front = tkinter.PhotoImage(file= myPreset['flashCard'])
card_back = tkinter.PhotoImage(file= myPreset['flashCardFlipped'])
flashcardImage = canvas.create_image(200,200, image=card_front)
flashcardTitle = canvas.create_text(200,120, text="Title", font=myFont1, fill=myPreset['textColor'])
flashcardWord = canvas.create_text(200,230, text="Word", font=myFont2, fill=myPreset['textColor'])

canvas.config(bg=myPreset['background'],highlightthickness=0)
canvas.grid(pady=10, row=0,column=0, columnspan=2)

wrong_mark = tkinter.PhotoImage(file='images/wrong.png')
wrong_mark_pressed = tkinter.PhotoImage(file='images/wrong_pressed.png')
wrong_button = tkinter.Button(image= wrong_mark, bg=myPreset['background'], bd=0, highlightthickness=0, activebackground=myPreset['background'],
                              command = nextCard)
wrong_button.bind("<Button-1>", lambda click: wrong_button.configure(image=wrong_mark_pressed))
wrong_button.bind("<ButtonRelease-1>", lambda click: wrong_button.configure(image=wrong_mark))
wrong_button.grid(pady=10, row=1,column=0)

right_mark = tkinter.PhotoImage(file='images/right.png')
right_mark_pressed = tkinter.PhotoImage(file='images/right_pressed.png')
right_button =tkinter.Button(image= right_mark, bg=myPreset['background'], bd=0, highlightthickness=0, activebackground=myPreset['background'],
                             command = isLearned)
right_button.bind("<Button-1>", lambda click: right_button.configure(image=right_mark_pressed))
right_button.bind("<ButtonRelease-1>", lambda click: right_button.configure(image=right_mark))
right_button.grid(pady=10, row=1,column=1)

nextCard()

window.mainloop()
