print("Выберите способ нахождения площади треугольника:")
print("1. Формула Герона")
print("2. По высоте и основанию")
option = int(input())

def triangleGeron(a, b, c):
    p = (a + b + c) / 2.0
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return round(S, 2)

def triangle(a, h):
    S = (a * h) / 2.0
    return round(S, 2)

if (option == 1):
    print("введите через пробел стороны треугольника: ")
    a, b, c = input().split(' ')
    print('Площдаь треугольника по Герону: ' + str(triangleGeron(float(a), float(b), float(c))))
elif (option == 2):
    print("введите через пробел основание и высоту треугольника: ")
    a, h = input().split(' ')
    print('Площдаь треугольника: ' + str(triangle(float(a), float(h))))