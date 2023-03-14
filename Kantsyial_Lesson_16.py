# Калькулятор. Создать класс, где реализованы методы математических операция (+-/*)
# и функция (вне класса) для ввода данных.
print('     Калькулятор ')
class Calculator:

    def my_sum(self, n, m):
        print (n + m)

    def my_dif(self, n, m):
        print (n - m)

    def my_mult(self, n, m):
        print (n * m)

    def my_div(self, n, m):
        try:
            print (n / m)
        except ZeroDivisionError:
            print('На ноль делить нельзя!')

    def my_input(self):

        while True:
            try:
                a = int(input('Введите первое число: '))
                break

            except ValueError:
                print('Неправильное число!')
                continue

        while True:
            try:
                c = int(input('Введите второе число: '))
                break

            except ValueError:
                print('Неправильное число!')
                continue

        while True:
            b = input('Введите знак операции (+,-,*,/): ')
            if not b in ('+-*/'):
                ('Неправильный знак операции!')
            else:
                if b == '+': b = self.my_sum(a, c)
                elif b == '-': b = self.my_dif(a, c)
                elif b == '*': b = self.my_mult(a, c)
                elif b == '/': b = self.my_div(a, c)
                else: print('Неправильный знак операции!')
                break

My_calculator = Calculator()
print(My_calculator.my_input())
