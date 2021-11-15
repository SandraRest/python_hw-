revenue = int(input('Введите значение выручки - '))
costs = int(input('Введите значение издержек - '))
result = revenue - costs
if result > 0:
    print(f"Прибыль {result}")
    print(f"Рентабельность {revenue/costs*100} %")
    personal = int(input('Введите численность работников - '))
    print(f"Прибль на одного работника - {result/personal}")
if result < 0:
    print(f"Убыток {-result}")