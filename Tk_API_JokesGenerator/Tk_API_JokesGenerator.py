import tkinter
import requests

class Card():
    def __init__(self):
        self.card_number = 0
    def pickCard(self):
        if self.card_number == 0:
            self.card_number = 1
            return 0
        elif self.card_number == 1:
            self.card_number = 2
            return 1
        elif self.card_number == 2:
            self.card_number = 0
            return 2

def sayJoke():
    try:
        get_data=requests.get('https://official-joke-api.appspot.com/random_joke')
        data = get_data.json()
        joke = data['setup']
        joke_punchline = data['punchline']
        my_canvas.itemconfig(jokecard_joke,text=joke)
        my_canvas.itemconfig(jokecard_punchline,text=joke_punchline)
        my_canvas.itemconfig(joke_card,image=joke_card_pic_list[my_card.pickCard()])
    except:
        print("Something went wrong!🥹")


myFont1 = ("Prestige Elite Std", 13, "italic")
myFont2 = ("Minion Pro", 18, "normal")
background_color = 'peach puff'
my_card = Card()

window = tkinter.Tk()
window.title("Jokes Generator")
window.config(padx=20, pady=20, bg= background_color)

my_canvas = tkinter.Canvas(width=202, height=236)
joke_card_pic1 = tkinter.PhotoImage(file= 'images/card1.png')
joke_card_pic2 = tkinter.PhotoImage(file= 'images/card2.png')
joke_card_pic3 = tkinter.PhotoImage(file= 'images/card3.png')
joke_card_pic_list = [joke_card_pic1, joke_card_pic2, joke_card_pic3]
joke_card = my_canvas.create_image(101,118, image=joke_card_pic_list[my_card.pickCard()])
jokecard_joke = my_canvas.create_text(115,70, text="Hello Beautiful Human!", font=myFont1, width=140)
jokecard_punchline = my_canvas.create_text(115,170, text="Wanna hear a joke?", font=myFont2, width=140)

my_canvas.config(bg=background_color, highlightthickness=0)
my_canvas.grid(pady=10, row=0,column=0, columnspan=2)

button_mark = tkinter.PhotoImage(file='images/button_active.png')
button_mark_pressed = tkinter.PhotoImage(file='images/button_deactive.png')
button = tkinter.Button(image= button_mark, bg=background_color,
                              bd=0, highlightthickness=0, activebackground=background_color,
                              command = sayJoke)
button.bind("<Button-1>", lambda click: button.configure(image=button_mark_pressed))
button.bind("<ButtonRelease-1>", lambda click: button.configure(image=button_mark))
button.grid(pady=10, row=1,column=0)

window.mainloop()