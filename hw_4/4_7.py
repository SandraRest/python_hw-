def factorial_gen(num):
    f_num = 1
    for i in range(num + 1):
        yield f"{i}! = {f_num}"
        f_num *= i + 1

    for el in factorial_gen(int(input("Факториал числа: "))):
        print(el)
