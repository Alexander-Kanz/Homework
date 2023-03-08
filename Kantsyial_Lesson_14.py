# №1. Если в функцию передаётся кортеж, то посчитать длину всех его строк.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Строка – кол-во букв.
# Сделать проверку со всеми этими случаями.
# Использовать готовые типы данных, с клавиатуры ничего не вводится
# Например function([1,2,3,'a','bc8?']) -> 4 числа, 3 буквы
# function((1,2,3,'a','bc8?',7,8,9)) -> 5 символов
# function(788) -> 1
# function('788') -> 0 букв
# №2. Привяжите к предыдущей функции декоратор, который будет выводить информацию о том,
# какой тип данных вы отправили: кортеж, список, число, строку или какой-то другой тип данных

numbers = 0
letters = 0
symbols = []
odd = 0
letters_str = 0
def type_func(fn):
    def wrapper(a):
        print('Тип данных ', type(a))
        fn(a)
    return wrapper

@ type_func
def my_func(a):
    global numbers, letters, symbols, odd, letters_str

    if type(a) == tuple:
        for i in a:
            if type(i) == str: symbols.append(len(i))
        print(sum(symbols), 'символов')

    elif type(a) == list:
        a = str(a)
        for i in a:
            if i.isdigit(): numbers += 1
            elif i.isalpha(): letters += 1
        print(numbers, 'числа,',letters, 'буквы')

    elif type(a) == int:
        for i in str(a):
            if int(i)%2 != 0: odd += 1
        print(odd, '- количество нечётных цифр')

    elif type(a) == str:
        for i in a:
            if i.isalpha(): letters_str += 1
        print(letters_str,'букв')

    else: print('Неизвестный тип данных')

my_func((1,2,3,'a','bc8?',7,8,9))
my_func([1,2,3,'a','bc8?'])
my_func(788)
my_func('788')
my_func(True)
my_func(3.14)