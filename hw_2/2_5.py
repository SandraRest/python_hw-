new_list = [8, 7, 7, 6, 6, 5, 4, 3, 3, 1]
number = int(input("Введите новый элемент рейтинга из натуральных чисел - "))
i = 0
for n in new_list:
    if number <= n:
        i += 1
    elif number > n:
        break
new_list.insert(i, float(number))
print(new_list)