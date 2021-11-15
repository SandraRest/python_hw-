num = int(input('Введите целое положительное число - '))
maximum = num % 10
while num > 0:
    digit = num % 10
    if digit > maximum:
        maximum = digit
        if digit == 9:
            break
        print(num)

print(f"Наибольшая цифра в числе {num} равна {maximum}")