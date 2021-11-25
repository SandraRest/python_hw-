my_list = [12, 8, 8, 23, 1, 499, 44, 3, 2, 499, 1, 4, 11]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(f"Элементы списка:\n", new_list)
