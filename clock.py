from tkinter import*
from time import strftime
from tkinter.ttk import*
window= Tk()
window.title("Clock")
window.geometry("300x200")
clock= Label(window)
clock.place(x=10,y=10)
def timeclock():
    s= strftime("%H:%M:%S %p")
    clock.config(text=s)
    clock.after(1000,timeclock)
timeclock()
window.mainloop()