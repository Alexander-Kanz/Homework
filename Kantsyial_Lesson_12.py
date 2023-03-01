# 1. Напишите функцию, которая принимает на вход два аргумента и возвращает их сумму.

def sum_1(a,b): return a+b

# 2. Напишите функцию, которая принимает на вход список чисел и возвращает их среднее значение.

def average(*list_1):
    sum_list_1 = 0
    for i in list_1:
        sum_list_1 += i
    return sum_list_1 / len(list_1)

# 3. Напишите функцию, которая принимает на вход число и возвращает True, если оно четное, и False, если оно нечетное.

def odd_or_even(c): return (True,False)[c%2] # решал что-то похожее на codewars.com

# 4. Напишите функцию, которая принимает на вход список и возвращает новый список, содержащий только уникальные элементы из исходного списка.

def my_set(*list_2): return set(list_2)

# 5. Решите задачу с использованием вложенной функции is_square. Предположим, у нас есть список чисел и мы хотим найти все числа,
#    которые являются квадратами других чисел в этом списке.

''' не смог придумать куда второй def засунуть'''

def find_square_numbers(numbers = 26):
    numbers = [*range(numbers)]
    return numbers
print(find_square_numbers())
number = []
for j in find_square_numbers():
    if j ** 2 in find_square_numbers():
        number.append(j ** 2)
print(f'{number}- числа, которые являются квадратами других чисел')




