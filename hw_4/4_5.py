from functools import reduce


def my_list(x, y):
    return x * y


new_list = [i for i in range(100, 1001, 2)]
print(f"List\n{new_list}\n{reduce(my_list, new_list)}")
