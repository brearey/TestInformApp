a = float(input())
b = float(input())
operator = str(input())
if operator == '+':
    print(a + b)
elif operator== '-':
    print(a - b)
elif operator== '*':
    print(a * b)
elif operator== '/' and b==0:
    print("Деление на 0!")
elif operator== '/' and b!=0:
    print(a / b)
elif operator== 'mod' and b==0:
    print('Деление на 0!')
elif operator== 'mod' and b!=0:
    print(a % b)
elif operator== 'pow':
    print(a ** b)
elif operator== 'div' and b==0:
    print('Деление на 0!')
elif operator== 'div' and b!=0:
    print(a // b)