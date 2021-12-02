class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname + ' ' + self.position

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


p = Position("Иван", "Иванов", "Директор", '100000', '30000')
print(p.get_full_name(), p.get_total_income())
