def my_sum():
    s = 0
    while True:
        numbers = input("Введите строку чисел или * для выхода: ").split()
        for i in numbers:
            try:
                if i == '*':
                    return
                else:
                    s += int(i)
            except ValueError:
                print('Введите число или *')
        print(f'Сумма {s}')
print(my_sum())
