a = float(input('Введите первое число'))  #Ввод первого числа
b = float(input('Введите второе число'))  #Ввод второго числа
print('Список действий: +,-,*,pow,/,div,mod') # Вывод списка команд для пользователя
c = str(input('Введите действие')) # Ввод действия

'''
условия, чтобы калькулятор работал
'''
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
