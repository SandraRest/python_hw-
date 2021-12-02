class Car:
    direction = ["север", "юг", "запад", "восток"]

    def __init__(self, name, speed, color, police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = police
        print(f'Машина: {name} цвет: {color}.\nПолицейская машина? {police}')

    def go(self):
        print(f'{self.name} Машина поехала.')

    def stop(self):
        print(f'{self.name} Машина остановилась.')

    def turn(self, direction):
        print(f'{self.name} Машина повернула {(self.direction)}.')

    def show_speed(self):
        return f'{self.name}: Текущая скорость: {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nВы превысили скорость! Ваша скорость составляет {self.speed}'
        else:
            return f'Скорость {self.name} нормальная'


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nВы превысили скорость! Ваша скорость составляет {self.speed}'
        else:
            return f'Скорость {self.name} нормальная'


class SportCar(Car):
    pass

class PoliceCar(Car):

    def __init__(self, name, speed, color, police=True):
        super().__init__(name, speed, color, police=True)

town = TownCar('Audi', 70, 'синий', False)
sport = SportCar('AudiRS', 170, ',белый', False)
work = WorkCar('Газель', 30, 'черный', False)
police = PoliceCar('Kia', 100, 'желтый', True)

list_cars = [town, sport, work, police]

for i in list_cars:
    i.go()
    print(i.show_speed())
    i.stop()
    print()

