import tkinter

window = tkinter.Tk()
window.title("Converter Tool")
window.config(padx=40, pady=40, bg='navajo white')
my_font = ('fixedsys',15,'normal')

def Miles2Kilometer():
    window.destroy()
    miles_to_km_converter()
def Celsius2Fahrenheit():
    window.destroy()
    celsius_to_fahrenheit_converter()
def Kilogram2Pound():
    window.destroy()
    kilogram_to_pound_converter()
def Litre2Gallon():
    window.destroy()
    litre_to_gallon_converter()
def Inch2Centimetre():
    window.destroy()
    inch_to_centimetre_converter()
def Acre2Bigha():
    window.destroy()
    acre_to_bigha_converter()

def main():
    converter1 = tkinter.Button(text="Miles to Kilometer", font=my_font,padx=10, pady=10, command=Miles2Kilometer,
                                fg = 'white', bg = 'salmon', bd=3,
                                activebackground = 'dark salmon',activeforeground = 'white')
    converter1.grid(column=1,row=1,sticky="ew")

    converter2 = tkinter.Button(text="Celsius to Fahrenheit", font=my_font,padx=10, pady=10, command=Celsius2Fahrenheit,
                                fg = 'white', bg = 'dark orange', bd=3,
                                activebackground = 'DarkOrange2',activeforeground = 'white')
    converter2.grid(column=1,row=2,sticky="ew")

    converter3 = tkinter.Button(text="Kilogram to Pound", font=my_font,padx=10, pady=10, command=Kilogram2Pound,
                                fg = 'white', bg = 'firebrick1', bd=3,
                                activebackground = 'firebrick3',activeforeground = 'white')
    converter3.grid(column=1,row=3,sticky="ew")

    converter4 = tkinter.Button(text="Litre to Gallon", font=my_font,padx=10, pady=10, command=Litre2Gallon,
                                fg = 'white', bg = 'deepskyblue2', bd=3,
                                activebackground = 'deepskyblue3',activeforeground = 'white')
    converter4.grid(column=1,row=4,sticky="ew")

    converter5 = tkinter.Button(text="Inch to Centimetre", font=my_font,padx=10, pady=10, command=Inch2Centimetre,
                                fg = 'white', bg = 'MediumOrchid1', bd=3,
                                activebackground = 'MediumOrchid3',activeforeground = 'white')
    converter5.grid(column=1,row=5,sticky="ew")

    converter6 = tkinter.Button(text="Acre to Bigha", font=my_font,padx=10, pady=10, command=Acre2Bigha,
                                fg = 'white', bg = 'OliveDrab3', bd=3,
                                activebackground = 'OliveDrab4',activeforeground = 'white')
    converter6.grid(column=1,row=6,sticky="ew")

def go_back():
    window.destroy()
    window.update()
    window.config(padx=20,pady=20,bg='navajo white')
    main()

def miles_to_km_converter():
    def miles_to_km():
        miles = float(miles_input.get())
        km = miles*1.60934
        kilometer_result_label.config(text= f'{km}')
    miles_input = tkinter.Entry()
    miles_input.grid(column=1, row=0)
    miles_label = tkinter.Label(text='Miles',font = my_font, padx=10, pady=10)
    miles_label.grid(column=2,row=0)
    is_equal = tkinter.Label(text='=', font= my_font, padx=10, pady=10)
    is_equal.grid(column=0, row=1)
    kilometer_label = tkinter.Label(text='Km', font=my_font, padx=10, pady=10)
    kilometer_label.grid(column=2,row=1)
    kilometer_result_label = tkinter.Label(text='0', font=my_font, padx=10, pady=10)
    kilometer_result_label.grid(column=1,row=1)
    calculate_button = tkinter.Button(text='Caculate', font=my_font, command=miles_to_km)
    calculate_button.grid(column=1,row=2 ,padx=10, pady=10)
    back_button=tkinter.Button(text='Back',font=my_font,command=go_back)
    back_button.grid(column=0,row=3,padx=10,pady=10)

def celsius_to_fahrenheit_converter():
    def celsius_to_fahrenheit():
        C = float(celsius_input.get())
        F = (C*9/5)+32
        fahrenheit_result_label.config(text= f'{F}')
    celsius_input = tkinter.Entry()
    celsius_input.grid(column=1, row=0)
    celsius_label = tkinter.Label(text='°Celcius',font = my_font, padx=10, pady=10)
    celsius_label.grid(column=2,row=0)
    is_equal = tkinter.Label(text='=', font= my_font, padx=10, pady=10)
    is_equal.grid(column=0, row=1)
    fahrenheit_label = tkinter.Label(text='°Fahrenheit', font=my_font, padx=10, pady=10)
    fahrenheit_label.grid(column=2,row=1)
    fahrenheit_result_label = tkinter.Label(text='0', font=my_font, padx=1, pady=1)
    fahrenheit_result_label.grid(column=1,row=1)
    calculate_button = tkinter.Button(text='Caculate', font=my_font, command=celsius_to_fahrenheit)
    calculate_button.grid(column=1,row=2 ,padx=10, pady=10)
    back_button=tkinter.Button(text='Back',font=my_font,command=go_back)
    back_button.grid(column=0,row=3,padx=10,pady=10)

def kilogram_to_pound_converter():
    def kilogram_to_pound():
        kg = float(kg_input.get())
        pound = kg*2.20462
        pound_result_label.config(text= f'{pound}')
    kg_input = tkinter.Entry()
    kg_input.grid(column=1, row=0)
    kg_label = tkinter.Label(text='Kg',font = my_font, padx=10, pady=10)
    kg_label.grid(column=2,row=0)
    is_equal = tkinter.Label(text='=', font= my_font, padx=10, pady=10)
    is_equal.grid(column=0, row=1)
    pound_label = tkinter.Label(text='Pound', font=my_font, padx=10, pady=10)
    pound_label.grid(column=2,row=1)
    pound_result_label = tkinter.Label(text='0', font=my_font, padx=1, pady=1)
    pound_result_label.grid(column=1,row=1)
    calculate_button = tkinter.Button(text='Caculate', font=my_font, command=kilogram_to_pound)
    calculate_button.grid(column=1,row=2 ,padx=10, pady=10)
    back_button=tkinter.Button(text='Back',font=my_font,command=go_back)
    back_button.grid(column=0,row=3,padx=10,pady=10)

def litre_to_gallon_converter():
    def litre_to_gallon():
        litre = float(litre_input.get())
        gallon = litre*2.20462
        gallon_result_label.config(text= f'{gallon}')
    litre_input = tkinter.Entry()
    litre_input.grid(column=1, row=0)
    litre_label = tkinter.Label(text='Litre',font = my_font, padx=10, pady=10)
    litre_label.grid(column=2,row=0)
    is_equal = tkinter.Label(text='=', font= my_font, padx=10, pady=10)
    is_equal.grid(column=0, row=1)
    gallon_label = tkinter.Label(text='Gallon', font=my_font, padx=10, pady=10)
    gallon_label.grid(column=2,row=1)
    gallon_result_label = tkinter.Label(text='0', font=my_font, padx=1, pady=1)
    gallon_result_label.grid(column=1,row=1)
    calculate_button = tkinter.Button(text='Caculate', font=my_font, command=litre_to_gallon)
    calculate_button.grid(column=1,row=2 ,padx=10, pady=10)
    back_button=tkinter.Button(text='Back',font=my_font,command=go_back)
    back_button.grid(column=0,row=3,padx=10,pady=10)

def inch_to_centimetre_converter():
    def inch_to_centimetre():
        inch = float(inch_input.get())
        cm = inch*2.20462
        centimetres_result_label.config(text= f'{cm}')
    inch_input = tkinter.Entry()
    inch_input.grid(column=1, row=0)
    inch_label = tkinter.Label(text='Inch',font = my_font, padx=10, pady=10)
    inch_label.grid(column=2,row=0)
    is_equal = tkinter.Label(text='=', font= my_font, padx=10, pady=10)
    is_equal.grid(column=0, row=1)
    centimetres_label = tkinter.Label(text='Centimetre(cm)', font=my_font, padx=10, pady=10)
    centimetres_label.grid(column=2,row=1)
    centimetres_result_label = tkinter.Label(text='0', font=my_font, padx=1, pady=1)
    centimetres_result_label.grid(column=1,row=1)
    calculate_button = tkinter.Button(text='Caculate', font=my_font, command=inch_to_centimetre)
    calculate_button.grid(column=1,row=2 ,padx=10, pady=10)
    back_button=tkinter.Button(text='Back',font=my_font,command=go_back)
    back_button.grid(column=0,row=3,padx=10,pady=10)

def acre_to_bigha_converter():
    def acre_to_bigha():
        acre = float(acre_input.get())
        bigha = acre*1.613334802
        bigha_result_label.config(text= f'{bigha}')
    acre_input = tkinter.Entry()
    acre_input.grid(column=1, row=0)
    acre_label = tkinter.Label(text='Acre',font = my_font, padx=10, pady=10)
    acre_label.grid(column=2,row=0)
    is_equal = tkinter.Label(text='=', font= my_font, padx=10, pady=10)
    is_equal.grid(column=0, row=1)
    bigha_label = tkinter.Label(text='Bigha', font=my_font, padx=10, pady=10)
    bigha_label.grid(column=2,row=1)
    bigha_result_label = tkinter.Label(text='0', font=my_font, padx=1, pady=1)
    bigha_result_label.grid(column=1,row=1)
    calculate_button = tkinter.Button(text='Caculate', font=my_font, command=acre_to_bigha)
    calculate_button.grid(column=1,row=2 ,padx=10, pady=10)
    back_button=tkinter.Button(text='Back',font=my_font,command=go_back)
    back_button.grid(column=0,row=3,padx=10,pady=10)

main()
window.mainloop()