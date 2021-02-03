# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом
# премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
        self.wage = wage
        self.bonus = bonus

    def get_full_name(self):
        return self.name + self.surname

    def get_total_income(self):
        return self.wage + self.bonus


pupkin = Position("Vasiliy", "Pupkin", "God", 500000, 200000)
ivanov = Position("Ivan", "Ivanov", "manager", 137000, 5678)
petrov = Position("John", "Petrov", "accountant", 80000.5, 1200.99)

print(f"{ivanov.name}, {ivanov.surname}, {ivanov.position}, {ivanov.wage}, {ivanov.bonus}")

print(f"Income of the employee - {pupkin.get_full_name()}: {pupkin.get_total_income()}")
print(f"Income of the employee - {ivanov.get_full_name()}: {ivanov.get_total_income()}")
print(f"Income of the employee - {petrov.get_full_name()}: {petrov.get_total_income()}")
