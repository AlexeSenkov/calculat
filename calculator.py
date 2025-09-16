print("1.Сложение")
print("2.Вычитание")
print("3.множение")
print("4.Деление")
print("5.Целочисленное деление")
print("6.Остаток от деления")
print("7.Возведение в степень")
print("8.Равно")
print("9.не равно")
print("10.Больше")
print("11.Меньше")
print("12.Больше или равно")
print("13.Меньше или равно")
print("14.Логическое И")
print("15.Логическое ИЛИ")
print("16.Логическое не")
print("17.Побитовое И")
print("18.Побитовое ИЛИ")
print("19.Побитовое ИСКЛЮЧАЮЩЕЕ ИЛИ")
print("20.Побитовое не")
print("21.Сдвиг влево")
print("22.Сдвиг вправо")

num1=int(input("Введите первое число: "))
num2=int(input("Введите второе число: "))
nomerop = input("выберите номер:")

if nomerop=="1":
    result = num1 + num2
    print(result)
elif nomerop=="2":
    result = num1 - num2
    print(result)
elif nomerop=="3":
    result = num1 * num2
    print(result)
elif nomerop=="4":
    if num2==0:
        print("ошибка деление на ноль")
    else:
        result = num1/num2
        print(result)
elif nomerop=="5":
    if num2==0:
        print("ошибка деление на ноль")
    else:
        result = num1//num2
        print(result)
elif nomerop=="6":
    if num2==0:
        print("ошибка деление на ноль")
    else:
        result = num1%num2
        print(result)
elif nomerop=="7":
    result = num1**num2
    print(result)

elif nomerop=="8":
    result = num1==num2
    print(result)
elif nomerop=="9":
    result = num1!=num2
    print(result)
elif nomerop==">":
    result = num1>num2
    print(result)
elif nomerop=="10":
    result = num1>num2
    print(result)
elif nomerop=="11":
    result = num1<num2
    print(result)
elif nomerop=="12":
    result = num1>=num2
    print(result)
elif nomerop=="13":
    result = num1<=num2
    print(result)

    print("ошибка")

