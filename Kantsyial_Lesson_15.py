# 1. Создайте класс Person, который имеет атрибуты name и age,
# а также метод greet()(выводит приветствие на экран с именем персоны).
class Person:

    def __init__(self):
        self.name = 'Александр'
        self.age = 39

    def greet(self):
        print(f'Привет, {self.name}!')

person_1 = Person()
person_1.greet()

# 2. Создайте класс Car, который имеет атрибуты make, model и year,
# а также метод get_info()(возвращает строку, содержащую информацию о машине).

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"Страна производитель автомобиля - {self.make} \nМодель - {self.model} \nГод выпуска - {self.year}"

bmw = Car('Германия', 'Х-6', 2017)
print(bmw.get_info())