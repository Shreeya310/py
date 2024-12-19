from tkinter import*
window=Tk()
window.geometry('800x800')
label=Label(text='ENTER THE NUMBERS:')
label.place(x=300,y=130)
entry=Entry()
entry.place(x=300,y=160)
btn=Button(text='CALCULATE',bg='blue',fg='black')
btn.place(x=310,y=190)
labels=Label(text='THE NUMBER OF NOTES FOR THE ABOVE VALUE ARE:-')
labels.place(x=230,y=240)
label1=Label(text='500')
label1.place(x=230,y=300)
label2=Label(text='200')
label2.place(x=230,y=330)
label3=Label(text='100')
label3.place(x=230,y=360)
e1=Entry()
e1.place(x=300,y=300)
e2=Entry()
e2.place(x=300,y=330)
e3=Entry()
e3.place(x=300,y=360)

def calculator():
    global amount
    amount=int(Entry.get() )
    note500=amount//500
    amount%=500
    note200=amount//200
    amount%=200
    note100=amount//100


window.mainloop()
