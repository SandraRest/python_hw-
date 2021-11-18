number = int(input("Введите число: "))
new_list = [7, 4, 3, 2]
c = new_list.count(number)
for element in new_list:
    if c > 0:
        i = new_list.index(number)
        new_list.insert(i+c, number)
        break
    else:
        if number > element:
            j = new_list.index(element)
            new_list.insert(j, number)
            break
        elif number < new_list[len(new_list) - 1]:
            new_list.append(number)
print(new_list)