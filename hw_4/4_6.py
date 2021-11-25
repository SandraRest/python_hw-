from itertools import count, cycle

# первый вариант

print("Программа генерирует целые числа, начиная с указанного. Для генерации следующего повторения нажмите Enter. "
      "Для выхода нажмите '*'")
for i in count(int(input("Введите целое число: "))):
    print(i, end='')
    quit = input()
    if quit == "*":
        break

# Второй вариант

print("Программа повторяет элементы списка")
my_list = input("Введите элементы, разделённые пробелом: ").split()
iter = cycle(my_list)
for i in range(len(my_list) * 5):  # 5 раз
    print(next(iter), end='')
