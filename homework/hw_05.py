# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title: str
    def __init__(self, title: str):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print(f"Пишем ручкой")

class Pencil(Stationery):
    def draw(self):
        print(f"Рисуем карандашом")

class Handle(Stationery):
    def draw(self):
        print(f"Рисуем маркером")


pen = Pen("Ручка")
pencil = Pencil("Карандаш")
handle = Handle("Маркер")
photo = Stationery("Фото")

photo.draw()
pen.draw()
pencil.draw()
handle.draw()

