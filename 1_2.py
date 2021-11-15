time = int(input('Введите время в секундах - '))
hour = time // 3600
min = (time // 60 - (hour * 60))
sec = time % 60
print(f"{hour:02}:{min:02}:{sec:02}")