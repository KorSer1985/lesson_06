"""
4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""


class Car:
    speed: int = 0
    color: str = "eggplant"
    name: str = "lambarzhiguli"
    is_police: bool = False

    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, s_speed):
        self.speed = s_speed
        return print(f"{self.name} started moving")

    def stop(self):
        self.speed = 0
        return print(f"The {self.name} stopped")

    def turn(self, direction: str):
        return print(f"{self.name} is heading {direction}")

    def show_speed(self):
        if self.speed == 0:
            return print(f"The car is not moving")
        else:
            return print(f"{self.name} moving at a speed of {self.speed}")


class TownCar(Car):
    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed == 0:
            return print(f"The car is not moving")
        elif self.speed <= 60:
            return print(f"{self.name} moving at a speed of {self.speed}")
        else:
            return print(f"{self.name} exceeded the speed limit on {self.speed - 60} km")


class SportCar(Car):
    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed == 0:
            return print(f"The car is not moving")
        elif self.speed <= 40:
            return print(f"{self.name} moving at a speed of {self.speed}")
        else:
            return print(f"{self.name} exceeded the speed limit on {self.speed - 40} km")


class PoliceCar(Car):
    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)


lada = TownCar(89, "Orange", "Vesta", False)
lamborghini = SportCar(280, "Red", "Aventador", False)
gaz = WorkCar(35, "White", "Next", False)
porsche = PoliceCar(300, "White", "911", True)

print(f"{lada.name}, {lada.color}, {lada.speed}, {lada.is_police}")
print(f"{lamborghini.name}, {lamborghini.color}, {lamborghini.speed}, {lamborghini.is_police}")
print(f"{gaz.name}, {gaz.color}, {gaz.speed}, {gaz.is_police}")
print(f"{porsche.name}, {porsche.color}, {porsche.speed}, {porsche.is_police}")

lada.go(50)
lada.turn("right")
lada.stop()
lada.show_speed()
lada.go(90)
lada.show_speed()
porsche.show_speed()
gaz.show_speed()
lamborghini.go(200)

"""
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""
