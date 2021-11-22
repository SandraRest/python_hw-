def my_func_1(x, y):    #вариант 1
    return x ** y


print(f'Возведения степени вариантом 1: '
      f'{my_func_1(int(input("Положительное число x: ")), int(input("Отрицательное число y: ")))}')


def my_func_2(x, y):     #вариант 2
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >= 0:
            return 'Не выполнено условие ввода:\nx должен быть больше 0\ny должен быть меньше 0'
        else:
            result = 1
            for _ in range(abs(y)):
                result = result * (1 / x)
            return f'Результат возведения x в степень y: {round(result, 4)}'
    except ValueError:
        return "Ошибка"


num_1 = input("Введите положительное число x: ")
num_2 = input("Введите отрицательное число y: ")
print(my_func_2(num_1, num_2))
