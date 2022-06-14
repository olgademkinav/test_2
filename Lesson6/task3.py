class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return (f'Имя{self.name}, Фамилия{self.surname}')

    def get_total_income(self):
        return sum(self._income.values())


workers = Position("Ольга", "Демкина", "доцент", 10000, 5000)
print(workers.get_full_name)
print(workers.position)
print(workers.get_total_income)
