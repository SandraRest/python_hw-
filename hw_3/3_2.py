def personal_info(**kwargs):
    return ' '.join(kwargs.values())


print(personal_info(name=input("Введите ваше имя: "), surname=input("Введите вашу фамилию: "),
                    birthday=input("Введите дату рождения: "), city=input("Введите ваш город: "),
                    email=input("Введите ваш email: "), phone=input("Введите ваш телефон: ")))
