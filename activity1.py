from tkinter import *

window = Tk()
window.title('Tinker Sample Window')
window.geometry('300x300')

#Lable
greeting = Label(text="Hello", fg='black' , bg='white')
#Button
button= Button(text="click me", fg='white' , bg='black')
#Entry
entry = Entry(fg='pink' , bg='blue' , width=50)

greeting.pack()
button.pack()
entry.pack()

frame=Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()
label = Label(master=frame, text='Sample Frame')
label.pack()

textbox = Text(fg='green',bg='yellow')
textbox.pack()

window.mainloop()