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
#Widgets
questionText = Label()
scoresText = Label()
btn0 = Button()
btn1 = Button()
btn2 = Button()
btn3 = Button()

#Scores
scores = 0
#root.geometry('400x400')

def generateQuestion(root, questionNumber):
    global btn0, btn1, btn2, btn3, questionText, scoresText, scores
    scoresText = Label(root, text='Ваши очки: '+str(scores))
    scoresText.grid(row=0, column=6, padx=30, pady=10)
    questionText = Label(root, text=questionAll[questionNumber])
    questionText.grid(row=1, column=0, columnspan=6, padx=20, pady=20)
    def btn1Clicked():
        checkAnswer(questionNumber, 1)
    def btn2Clicked():
        checkAnswer(questionNumber, 2)
    def btn3Clicked():
        checkAnswer(questionNumber, 3)
    def btn4Clicked():
        checkAnswer(questionNumber, 4)

    btn0 = Button(root, text=answerTextAll[questionNumber][0])
    btn0.grid(row=2, padx=10, pady=10)
    btn0.config(command=btn1Clicked)

    btn1 = Button(root, text=answerTextAll[questionNumber][1])
    btn1.grid(row=3, padx=10, pady=10)
    btn1.config(command=btn2Clicked)

    btn2 = Button(root, text=answerTextAll[questionNumber][2])
    btn2.grid(row=4, padx=10, pady=10)
    btn2.config(command=btn3Clicked)

    btn3 = Button(root, text=answerTextAll[questionNumber][3])
    btn3.grid(row=5, padx=10, pady=10)
    btn3.config(command=btn4Clicked)

def checkAnswer(questionNumber, i):
    global scores, scoresText, root, stepNumber
    if (i == answerAll[questionNumber]):
        #messagebox.showinfo('Информация', 'Правильно!')
        scores = scores + 1
        scoresText = Label(root, text='Ваши очки: ' + str(scores))
        scoresText.grid(row=0, column=6, padx=30, pady=10)
        if (messagebox.showinfo('Test', 'Test')): destroyAll()
    else:
        if messagebox.showerror('Test', 'Test'): destroyAll()

#for i, word in enumerate(questionAll):
#    generateQuestion(root, i)
generateQuestion(root, 0)
stepNumber = 0
def destroyAll():
    global btn0, btn1, btn2, btn3, questionText, root, stepNumber, questionAll, scores, scoresText
    questionText.destroy()
    scoresText.destroy()
    btn0.destroy()
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    stepNumber = stepNumber + 1
    if (stepNumber > len(questionAll)-1):
        if (messagebox.showinfo('Тест закончен', 'Ваши очки: '+str(scores))):
            root.quit()
    else:
        generateQuestion(root, stepNumber)

root.mainloop()