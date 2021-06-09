with open('file.txt') as textFile:
    linesCount = 0

    for line in textFile:
        linesCount = linesCount + 1
        print("Количество слов в строке: ", len(line.split(',')))
        print("Количество символов в строке: ", len(line))

print("Количество строк: ", linesCount)