def int_func(word):
    ls = []
    for i in range(len(word)):
        ls.append(word[i][0:1].title() + word[i][1:])
    return ' '.join(ls)


print(int_func(input("Введите текст: ").split()))
