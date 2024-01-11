import tkinter
import csv
from tkinter import messagebox
import PasswordGenerator

def create_password():
    my_pass = PasswordGenerator.generate_password()
    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, my_pass)
def save_password():
    website = str(website_entry.get())
    email = email_entry.get()
    password = password_entry.get()
    if len(website)<1 or len(email)<1 or len(password)<1:
        is_empty = True
        messagebox.showerror(title="Error", message="EMPTY FIELD(s) FOUND!")
    else:
        is_empty = False
    if not is_empty:
        confirmation = messagebox.askokcancel(title='Addition Status', message='Entered Informations:\n'+f'➡️ Website : {website}\n➡️ Email : {email}\n➡️ Password :{password}\n<<<Confirm Entry?>>>')
        if confirmation:
            with open('passwords.csv',"a") as data:
                website_entry.delete(0,tkinter.END)
                password_entry.delete(0, tkinter.END)
                write_csv = csv.writer(data, lineterminator = '\n')
                write_csv.writerow([website, email, password])
        else:
            pass

def search_password():
    website = str(website_entry.get())
    email = email_entry.get()
    if len(website)<1 or len(email)<1 :
        is_empty = True
        messagebox.showerror(title="Error", message="You have enter website and email to get your password!!!")
    else:
        is_empty = False
    if not is_empty:
        with open('passwords.csv', mode="r") as data:
            website_entry.delete(0,tkinter.END)
            password_entry.delete(0,tkinter.END)
            csvfile = csv.reader(data)
            for line in csvfile:
                if website == line[0] and email == line[1]:
                    password = line[2]
                    messagebox.showinfo(title="Your Password", message= f"Your {website} password is \n <<<{password}>>>")
                    break
                else:
                    password = None
            if password == None:
                messagebox.showerror(title="Error",message="No Match Found!!!")


my_font1 = ('Helvetica',20, "bold")
my_font2 = ('Helvetica',12, "bold")

window = tkinter.Tk()
window.title("MY Password Manager 🧑‍💼")
window.config(padx=10,pady=10)

dummy1 = tkinter.Label(pady=125, padx=230,
                       bg='firebrick3', highlightthickness=0)
dummy1.grid(column=0,row=0,columnspan=3, sticky= 'nsew')
dummy2 = tkinter.Label(pady=80, padx=230,
                       bg='firebrick3', highlightthickness=0)
dummy2.grid(column=0,row=1,columnspan=4,rowspan=5, sticky= 'nsew')

canvas = tkinter.Canvas(height=250, width=250, highlightthickness=0, bg='firebrick3',  relief='ridge')
lock_logo = tkinter.PhotoImage(file='MyLock.png')
canvas.create_image(126,126, image=lock_logo)
canvas.grid(column=0,row=0, columnspan=3)

lock_label = tkinter.Label(padx=50,pady=2, text="My Password Manager", font=my_font1, highlightthickness=0,bg='firebrick3', fg='gray15' )
lock_label.grid(column=0,row=1,columnspan=3)

website_lab = tkinter.Label(    text='Website     :', font = my_font2, justify='center' ,bg='firebrick3', fg='gray15')
email_lab = tkinter.Label(      text='Email         :', font = my_font2, justify='center' ,bg='firebrick3', fg='gray15')
password_lab = tkinter.Label(   text='Password:', font = my_font2, justify='center' ,bg='firebrick3', fg='gray15')

website_lab.grid(column=0,row=2)
email_lab.grid(column=0,row=3)
password_lab.grid(column=0,row=4)

website_entry = tkinter.Entry(width=30, bg='gray20', fg='white')
email_entry = tkinter.Entry(width=59,bg='gray20', fg='white')
password_entry = tkinter.Entry(width=30,bg='gray20', fg='white')

website_entry.grid(column=1,row=2, columnspan=1)
email_entry.grid(column=1,row=3, columnspan=2)
password_entry.grid(column=1,row=4)

email_entry.insert(0, "myemail@anymail.com")

search_button= tkinter.Button(text='Search Password', font=('Times new roman',9, "normal"),padx=32, height=1,
                                bg='salmon',bd=3,activebackground='indian red',
                                command=search_password)
search_button.grid(column=2,row=2)

generate_button= tkinter.Button(text='Generate Password', font=('Times new roman',9, "normal"),padx=32, height=1,
                                bg='gold',bd=3,activebackground='goldenrod',
                                command=create_password)
generate_button.grid(column=2,row=4)

add_button = tkinter.Button(text='Add', font=('Times new roman',10, "normal"), highlightthickness=0, padx=212,
                            bg='yellow green',bd=3, activebackground = 'olive drab',
                            command=save_password)
add_button.grid(column=0,row=5,columnspan=3)

window.mainloop()