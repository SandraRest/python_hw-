with open('text_2.txt', 'r', encoding='utf-8') as f:
    staff_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Средняя зарплата = {round(sum(staff_dict.values()) / len(staff_dict), 2)}\n'
          f'Сотрудники с зарплатой меньше 20000р {[s[0] for s in staff_dict.items() if s[1] < 20000]}')