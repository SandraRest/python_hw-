my_f = open('test.txt', 'w')
line = input('Введите текст или пустую строку: \n')
while line:
    my_f.writelines(line)
    line = input('Введите текст или пустую строку: \n')
    if not line:
        break
        my_f.close()
        my_f = open('test.txt', 'r')
        content = my_f.readlines()
        print(content)
        my_f.close()
