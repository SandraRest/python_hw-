day = 1
start = float(input('Начальный результат - '))
last = float(input('Конечный результат - '))
if start <= 0 or last <= 0:
    print('Введенный результат неверный')
else:
    while start < last:
        start *= 1.1
        day += 1
        print(f'Спортсмен достиг результата за {day} дня')