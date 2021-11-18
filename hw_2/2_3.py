month = input("Введите месяц цифрой - ")
if month .isdigit() and 0 < int(month) <= 12:
    season_1 = ['зима', "весна", "лето", "осень", "зима"]
    season_2 = {0: "зима", 1: "весна", 2: "лето", 3: "осень", 4: "зима"}
    print(f"Сезон {season_2[int(month) // 3]}")
else:
    print("Неверное число")