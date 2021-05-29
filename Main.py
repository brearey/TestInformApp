from tkinter import *
root = Tk()
root['bg'] = '#fafafa'
root.title('Тест по информатике')
root.geometry('300x250')
root.resizable(width=False, height=False)

canvas = Canvas(root, height=300, width=250)
canvas.pack()

frame = Frame(root, bg='red')
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

title = Label(frame, text='Подсказка', bg='gray', font=40)
title.pack() #.place() .grid()
btn = Button(frame, text='Нажми меня', bg='yellow')
btn.pack()
root.mainloop()