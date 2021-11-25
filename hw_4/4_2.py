my_list = [40, 7, 3, 4, 2, 2, 15, 22, 7]
new_list = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]
print(new_list)
