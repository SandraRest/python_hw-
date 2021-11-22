def my_func(a, b, c):
    print(f'Сумма двух наибольших аргументов равна: {a + b + c - min([a, b, c])}')


my_func(int(input("a: ")), int(input("b: ")), int(input("c: ")))
