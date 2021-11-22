def div(a, b):
    try:
        a, b = int(a), int(b)
        return a / b
    except ValueError:
        return "Ошибка"
    except ZeroDivisionError:
        return "Делить на ноль нельзя!"


print(div((input("Введите первое число: ")), (input("Введите второе число: "))))
