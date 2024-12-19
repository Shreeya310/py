from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
window=Tk()
window.title("IMAGE IN TKINTER")
window.geometry("400x400")
upload=Image.open('car-967387_1280.webp')
image=ImageTk.PhotoImage(upload)
label=Label(image=image,height=900,width=300)
label.place(x=100,y=100)
def msg():
    messagebox.showwarning("ALERT")
btn=Button(text="CLICK HERE",command=msg)    
btn.place(x=500,y=200)
window.mainloop()