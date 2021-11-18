string = input("Введите несколько слов через пробел - ") .split()
for i, word in enumerate(string, 1):
    print(f"{i}, {word[:10]}")