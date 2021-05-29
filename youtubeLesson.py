from tkinter import *
from tkinter import messagebox

# Вопросы и ответы
questionAll = [
    'Сколько бит памяти компьютера займет слово «информатика»?',
    'Информацию, не зависящую от чужого мнения, называют:',
    'Какое устройство ПК предназначено для ввода информации?'
]
answerTextAll = [
    ['11 бит', '80 бит', '8 бит', '88 бит'],
    ['достоверной', 'актуальной', 'объективной', 'полезной'],
    ['Процессор', 'Монитор', 'Клавиатура', 'Принтер']
]
answerAll = [
    4,
    3,
    3
]

root = Tk()
root.title('Тест по информатике')
#root.geometry('400x400')

def que_one():
    question = Label(root, text='Висит груша и её нельзя скушать?')
    answer = Entry()
    btn = Button(root, text='Ответить', command=lambda: game1())
    question.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
    answer.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
    btn.grid(row=2, column=1, columnspan=2, padx=10, pady=10)
    def game1():
        if answer.get() == 'Лампочка':
            que_two()
        else:
            #que_one()
            messagebox.showerror('Ошибка', 'Попробуй еще раз')


def que_two():
    question = Label(root, text='Зимой и летом одним цветом?')
    answer = Entry()
    btn = Button(root, text='Ответить')
    question.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
    answer.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
    btn.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

def generateQuestion(root, questionNumber):
    questionText = Label(root, text=questionAll[questionNumber])
    questionText.grid(row=0, column=0, columnspan=6, padx=20, pady=20)

    def btn1Clicked():
        checkAnswer(questionNumber, 1)
    def btn2Clicked():
        checkAnswer(questionNumber, 2)
    def btn3Clicked():
        checkAnswer(questionNumber, 3)
    def btn4Clicked():
        checkAnswer(questionNumber, 4)

    btn0 = Button(root, text=answerTextAll[questionNumber][0])
    btn0.grid(row=1, padx=10, pady=10)
    btn0.config(command=btn1Clicked)

    btn1 = Button(root, text=answerTextAll[questionNumber][1])
    btn1.grid(row=2, padx=10, pady=10)
    btn1.config(command=btn2Clicked)

    btn2 = Button(root, text=answerTextAll[questionNumber][2])
    btn2.grid(row=3, padx=10, pady=10)
    btn2.config(command=btn3Clicked)

    btn3 = Button(root, text=answerTextAll[questionNumber][3])
    btn3.grid(row=4, padx=10, pady=10)
    btn3.config(command=btn4Clicked)

def checkAnswer(questionNumber, i):
    if (i == answerAll[questionNumber]):
        messagebox.showinfo('Информация', 'Правильно!')
    else:
        messagebox.showerror('Ошибка', 'Ваш ответ неверный')

#for i, word in enumerate(questionAll):
#    generateQuestion(root, i)
generateQuestion(root, 0)
stepNumber = 0
def destroyAll():
    global stepNumber
    global root
    root.destroy()
    stepNumber = stepNumber + 1
    generateQuestion(root, stepNumber)
btn_next = Button(root, text='Следующий вопрос')
btn_next.grid(padx=20, pady=20, command=destroyAll())

root.mainloop()