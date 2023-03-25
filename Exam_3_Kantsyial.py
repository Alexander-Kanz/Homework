#1.	Создайте класс "Студент", который имеет атрибуты имя и возраст, а также методы "изменить_имя" и "изменить_возраст".
#   Напишите функцию, которая создает объект класса "Студент", запрашивая у пользователя его имя и возраст,
#   а затем предлагает пользователю изменить имя и возраст.
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def change_name(self, new_name): # метод изменить имя
        self.name = new_name
        return self.name

    def change_age(self, new_age): # метод изменить возраст
        self.age = new_age
        return self.age

    def __str__(self):
        return f'{self.name}, {self.age} лет'

Victor = Student('Виктор', 20)
print(Victor)
Victor.change_name('Алексей')
Victor.change_age(100)
print(Victor)

# 2. Напишите функцию, которая принимает на вход список чисел и возвращает сумму квадратов всех четных чисел в списке.

def sum_of_squares(*list_num):
    new_list = []
    for i in list_num:
        if i%2==0:
            new_list.append(i**2)
    return f'Cумма квадратов всех четных чисел в списке: {sum(new_list)}'

print(sum_of_squares(1,2,3,4,5,6,7,8,9))

# 3. Создайте класс "Калькулятор", который имеет атрибуты "значение" и методы "сложить", "вычесть", "умножить" и "разделить".
#    Напишите функцию, которая создает объект класса "Калькулятор" и позволяет пользователю выполнить несколько арифметических операций с его помощью.

class Calculator:

    def __init__(self, value_1, value_2):
        self.value_1 = value_1
        self.value_2 = value_2

    def my_sum(self):
        return f'Сумма чисел равна: {self.value_1 + self.value_2}'

    def my_dif(self):
        return f'Разность чисел равна: {self.value_1 - self.value_2}'

    def my_mult(self):
        return f'Произведение чисел: {self.value_1 * self.value_2}'

    def my_div(self):
        try:
            return f'Частное чисел: {self.value_1 / self.value_2}'
        except ZeroDivisionError:
            return 'На ноль делить нельзя!'

my_caclulator = Calculator(5,0)
print(my_caclulator.my_div())

# 4. Создайте класс "Автомобиль", который имеет атрибуты "марка", "модель", "год_выпуска", "цвет" и метод "описание",
#    который выводит описание автомобиля в виде строки. Напишите функцию, которая создает объект класса "Автомобиль",
#    запрашивая у пользователя информацию о марке, модели, годе выпуска и цвете, а затем выводит описание автомобиля.

class Car:
    def __init__(self, brand, model, year_of_issue, color):
        self.brand = brand
        self.model = model
        self.year_of_issue = year_of_issue
        self.color = color

    def __str__(self):
        return f'Марка: {self.brand}, Модель: {self.model}, Год выпуска: {self.year_of_issue}, Цвет: {self.color}'

car_1 = Car('BMW', 'x6', 2017, 'Black')
print(car_1)

# 5. Создайте класс "Сотрудник", который имеет атрибуты "имя", "фамилия", "должность" и метод "описание",
#    который выводит описание сотрудника в виде строки. Создайте класс "Отдел", который имеет атрибуты "название"
#    и "список_сотрудников", а также методы "добавить_сотрудника" и "удалить_сотрудника". Напишите функцию,
#    которая создает объект класса "Отдел", запрашивая у пользователя его название, а затем предлагает пользователю
#    добавить несколько сотрудников в отдел, после чего выводит список всех сотрудников в отделе и их описания.
#    Затем функция предлагает пользователю удалить одного из сотрудников и выводит обновленный список сотрудников и их описания.

class Employee:
    def __init__(self, name, surname, job_title):
        self.name = name
        self.surname = surname
        self.job_title = job_title

    def __str__(self):
        return f'Имя: {self.name}, Фамилия: {self.surname}, Должность: {self.job_title}'

class Department:
    def __init__(self, title, list_of_employees):
        self.title = title
        self.list_of_employees = list_of_employees

    def add_employee(self, add): # метод добавить сотрудника
        self.list_of_employees += add

    def __str__(self):
        return f"Cписок всех сотрудников в отделе: {self.list_of_employees}"

    def delete_employee(self,employee): # метод удалить сотрудника
        if employee in self.list_of_employees:
            del self.list_of_employees[employee]

employee_1 = Employee('Александр', 'Канцыял', 'Директор')
my_department = Department('best corporation', ['Иванов', 'Петров', 'Сидоров'])

print(employee_1)
print(my_department)
print(my_department.add_employee(['Чернов', 'Белов'])) #добавил сотрудника
print(my_department)
print(my_department.delete_employee(['Иванов']))
print((my_department))




