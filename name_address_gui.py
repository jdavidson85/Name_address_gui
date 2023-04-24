from tkinter import *
window = Tk()
window.title("GUI")
window.geometry('350x200')


label1 = Label(window, text="")
label1.grid(column=0, row=0)

label2 = Label(window, text="")
label2.grid(column=0, row=1)


def clicked():
    res1 = "Joseph Davidon"
    res2 = "1608 Brompton Ct, Crystal Lake"
    label1.configure(text=res1)
    label2.configure(text=res2)

bt = Button(window, text="Show Info", command=clicked)
bt.grid(column=0, row=3)

bt = Button(window, text="Quit", command=window.destroy)
bt.grid(column=1, row=3)

window.mainloop()
