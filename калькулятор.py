a = float(input('Введите первое число'))
b = float(input('Введите второе число'))
print('Список действий: +,-,*,pow,/,div,mod')
c = str(input('Введите действие'))

if c == "+":
    print(a+b)
elif c == "-":
    print(a-b)
elif c == "*":
    print(a*b)
elif c == "pow":
    print(a**b)
elif b == 0:
    print("Деление на 0! ")
elif c == "/":
    print(a/b)
elif c == "div":
    print(a//b)
elif c == "mod":
    print(a%b)
