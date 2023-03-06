# 1. Написать рекурсивную функцию, которая определяет, является ли строка палиндромом
# (одинаково читается в обе стороны: герег, лол, мам, level и тд.)

def is_palindrome(stroka):
    stroka = stroka.lower()
    if len(stroka) < 2:
        return True
    elif stroka[0] != stroka[-1]:
        return False
    else:
        return is_palindrome(stroka[1:-1])
print(is_palindrome('Level'))

def find_palindrome(string): # не рекурсивная!!!
    def revers_text(str): return str.lower()[-1::-1]
    return ('Не палиндром','Палиндром') [string.lower() == revers_text(string)]
print(find_palindrome('Level'))

#2. Написать рекурсивную функцию для подсчета количества элементов в списке.

def number_of_elements(my_list):
    if my_list !=0: return len(my_list)
    else: return 0
print(number_of_elements([1,2,3,4,5,5,4,3,2,1,'ewrwer']))

#3. Этот код отсортирует список строк по последнему символу в каждой строке.
    # Здесь использована лямбда-функция в качестве ключа в сортировке.
    # Измените код так, чтобы сортировка была по второму символу каждой строки
strings = ['apple', 'banana', 'cherry', 'date']
sorted_strings = sorted(strings, key=lambda s: s[1]) # s[-1] надо поменять на s[1], как я понял, но Output почему-то другой
print(sorted_strings) # Output: ['cherry', 'date', 'apple', 'banana']

#4. Напишите функцию make_adder(n),
# которая принимает целое число n и возвращает внутреннюю функцию,
# которая может прибавлять этот n к любому другому целому числу.

def make_adder(n):
    def adder(n2):
        return n + n2
    return adder
print(make_adder(3)(7))

#5. Напишите функцию counter(), которая возвращает внутреннюю функцию increment(),
# которая увеличивает счетчик на 1 каждый раз, когда она вызывается.

def counter(n):
    def increment(n2):
        return n + n2
    return increment
add_one = counter(1)
print(add_one(5))