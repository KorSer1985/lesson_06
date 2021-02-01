#### класс объект атрибут ########
'''
атрибуты класса
атрибуты объекта (экземпляра) класса
list.append(x)
'''
'''
class Car:
    """
    ###### публичный, защищенный, приватный (инкапсуляция)######
    x - Public
    _x - Protected
    __x - Private
    """
    color = 'red'
    model = 'camry'
    _count = 0

    def print_info(self):
        pass
        # print(self.__form_description())

    # def __form_description(self):
    #     return f"{self.color, self.model}"
    # ниже через магический метод __str__
    def __str__(self):
        return f"{self.color, self.model}"

    ###### инициализация и методы #######
    def __init__(self, color, model = None):
        """
        "магический метод"
        конструктор класса (точно такой же метод, создает объекты класса)
        """
        print("Hello, It's me!")
        Car._count += 1
        if model == None:
            self.model = Car.model
        else:
            self.model = model
        self.color = color

    def car_returned(self):
        Car._count -= 1

test1_car = Car('orange', 'audi') #вызов __init__
test2_car = Car('black', 'bmw') #red
test3_car = Car('yellow') #red

print(test1_car.color)
# test1_car.color = 'pink'

print(Car.color)
Car.color = 'blue'
test1_car.print_info()
# print(test1_car.__form_description())
test2_car.print_info()
test3_car.print_info()
print("Car:", test2_car)
str_test2_car = str(test2_car)
print("str_test2_car", str_test2_car)
print(Car._count)
test3_car.car_returned()
print(Car._count)
'''
##### наследование #######
class Shape:
    def __init__(self, color, param_1, param_2, rectangle_h = None):
        print("I am new shape!")
        self.color = color
        self.param_1 = param_1
        self.param_2 = param_2
        self.rectangle_h = rectangle_h

    def square(self):
        return self.param_1 * self.param_2

class Toy:
    def __init__(self, *args):
        print("I am toy")

    def play_sound(self):
        print("You win!")

class Rectangle(Shape):
    pass

class Triangle(Shape, Toy):
    """
    s = 1/2*h*a
    """
    def square(self):
        return 1/2 * self.param_1 * self.rectangle_h

test_rectangle = Rectangle("white", 10, 20)
print(test_rectangle.square())

test_triangle = Triangle("orange", 30, 2, 7)
print(test_triangle.square())
test_triangle.play_sound()


# class Triangle(Shape):
#     def __init__(self, color, param_1, param_2, triangle_p):
#         super().__init__(color, param_1, param_2)
#         self.triangle_p = triangle_p
#
#     def get_t_p(self):
#         return self.triangle_p
#
# r = Rectangle("white", 10, 20, True)
# print(r.color)
# print(r.square())
# print(r.get_r_p())
# t = Triangle("red", 30, 40, False)
# print(t.color)
# print(t.square())
# print(t.get_t_p())


###### полиморфизм и перегрузка методов########

######## пример класс #########
"""
id камеры (или путь до видео) 
калибровка - убрать искажение линзы
обрезать видео 
"""
# from cv2 import imread

class Video:
    def __init__(self, path):
        self.path = path
        # self.video = cv2.imread(path) #для картинки

    def calibration(self):
        """
        примняем кучу фнкций к self.video
        :return:
        """
        return new_video #объект класса

    def cut_frame(self):
        return new_video #не обязательно объект класса
        """
        обрезаем кадр
        :return:
        """
    def show_video(self):
        """
        показывает видео
        :return:
        """
main_video1 = Video('folder_1')
main_video2 = Video('folder_2')
main_video3 = Video('folder_3')

clean_video = main_video1.calibration()
clean_video = clean_video.cut_frame()

###пример нескольких методов подряд
# print(np.array(test_list).add(7).sum())

