my_file = open('test_1.txt')

with open("text_1.txt", encoding='utf-8') as f:
    my_line = f.readlines()
    for index, value in enumerate(my_file, 1):
        number_of_word = len(value.split())
        print(f'Строка {index} содержит {number_of_word} слов')
