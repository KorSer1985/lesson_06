# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только
# в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep


class TrafficLight:
    __color = "green"

    def running(self):
        while True:
            if self.__color != "green":
                print(f"Invalid operating mode of the traffic light")
                break
            self.__color = "red"
            print(f"The red light is on: {self.__color}")
            sleep(7)

            if self.__color != "red":
                print(f"Invalid operating mode of the traffic light")
                break
            self.__color = "yellow"
            print(f"The red light is on: {self.__color}")
            sleep(2)

            if self.__color != "yellow":
                print(f"Invalid operating mode of the traffic light")
                break
            self.__color = "green"
            print(f"The red light is on: {self.__color}")
            sleep(5)


run = TrafficLight()
print(run.running())
