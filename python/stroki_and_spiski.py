#Напиши функцию, которая 
#принимает строку и возвращает её в обратном порядке.

#решение со списком
def reverse_stroka(symbols):

    stroka = []

    for i in range(len(symbols) - 1, -1, -1):
        stroka.append(symbols[i])

    return stroka

print(reverse_stroka("asdfgh"))

#Напиши функцию, 
#которая считает количество символов в строке без использования len().
def character_count(symbols):

    count = 0 

    for symbol in symbols:
        count += 1

    return count

print(character_count("qwertyuiop"))

#временная сложность O(n), где  n - это количество символов во входной строке
#если строка содержит 10 символов, то цикл выполнится 10 раз и тд
#кол-во операций растет пропорционально длине строки, поэтому О(n)

#в функции есть 3 переменные - symbols, count, symbol
#Даже если передать строку из миллиона символов, нам по-прежнему достаточно счётчика 
#и текущего символа. Количество используемых переменных не увеличивается 
#вместе с размером входа.
#доп память - O(1)

#Напиши функцию, которая считает количество гласных букв в строке.
def count_vowels(symbols):

    count = 0

    for symbol in symbols:

        if symbol in 'euioay':
            count += 1

    return count

print(count_vowels("qwertyuio"))

#Напиши функцию, которая возвращает строку 
#в обратном порядке без использования срезов и списков.

#решение со строкой
def reverse_symbol(symbols):

    stroka = ""

    for i in range(len(symbols) - 1, - 1, -1):
        stroka += symbols[i]

    return stroka

print(reverse_symbol("qwerty"))

#Напиши функцию, которая проверяет, 
#является ли строка палиндромом. Регистр символов учитывать не нужно.
def is_palindrom(symbols):

    stroka = ""

    for i in range(len(symbols) - 1, - 1, - 1):
        stroka += symbols[i]

    if stroka == symbols:
        return True

    return False

print(is_palindrom("addas"))

#Напиши функцию, которая считает, 
#сколько раз заданный символ встречается в строке.

def count_symbols(symbols, target):

    count = 0 

    for symbol in symbols:
        if symbol == target:
            count += 1

    return count

print(count_symbols(("qwertqqrtjdq"), "q"))

#Напиши функцию, которая возвращает первый символ строки,
#который встречается в ней только один раз.

#решение с помощью двух списков
def one_symbol(symbols):

    for symbol in symbols:

        count = 0 

        for other_symbol in symbols:
            if other_symbol == symbol:
                count += 1

        if count == 1:
            return symbol

    return False

#решение с помощью словаря 
def one_symbol_1(symbols):

    dictionary = {}

    for symbol in symbols:
        if symbol in dictionary:
            dictionary[symbol] += 1
        else:
            dictionary[symbol] = 1

    for symbol in dictionary:
        if dictionary[symbol] == 1:
            return symbol

    return None

#с методом count()
def one_symbol_2(symbols):

    for symbol in symbols:

        if symbols.count(symbol) == 1:
            return symbol

    return None

#count() - считает вхождение подстроки
print("banana".count("a"))
#find() - находит индекс первого вхождения
print("banana".find("a"))
#rfind() - находит индекс последнего вхождения
print("banana".rfind("a"))
#index() - находит индекс, иначе вызывает ошибку
print("banana".index("a"))
#startswith() - проверяет начало строки
print("banana".startswith("ba"))
#endswith() - проверяет конец строки
print("banana".endswith("na"))


#lower() - переводит буквы в нижний регистр

#Напиши функцию is_anagram(first, second), которая проверяет, 
#являются ли две строки анаграммами друг друга.
def is_anagramm(firsts, seconds):

    glossary_first = {}
    glossary_second = {}

    for first in firsts.lower():
        if first not in glossary_first:
            glossary_first[first] = 1
        else:
            glossary_first[first] += 1

    for second in seconds.lower():
        if second not in glossary_second:
            glossary_second[second] = 1
        else:
            glossary_second[second] += 1

    return glossary_second == glossary_first
  
print(is_anagramm("listen", "silent"))

def is_anagramm_1(firsts, seconds):

    glossary = {}

    for first in firsts:
        if first in glossary:
            glossary[first] += 1
        else:
            glossary[first] = 1

    for second in seconds:
        if second in glossary:
            glossary[second] -= 1
        else:
            glossary[second] = -1

    for count in glossary.values():
        if count != 0:
            return False

    return True
print(is_anagramm_1("listen", "silent"))


#Напиши функцию most_frequent(symbols), которая 
#возвращает символ, встречающийся в строке чаще всего.
def most_frequent(symbols):

    glossary = {}

    for symbol in symbols.lower():
        if symbol in glossary:
            glossary[symbol] += 1
        else:
            glossary[symbol] = 1

    max_value = 0
    max_key = None
    
    for key, value in glossary.items():
        if value > max_value:
            max_value = value
            max_key = key

    return max_key

print(most_frequent("asdfdsaas"))

#Напиши функцию count_positive(numbers), которая принимает 
#список чисел и возвращает количество положительных чисел в нём.
def count_positive(numbers):

    count = 0

    for number in numbers:
        if number > 0:
            count += 1

    return count

print(count_positive([1, -4, 5, -10, 0, -3]))

#Напиши функцию, которая 
#удаляет все нули из списка без создания второго списка.
#со вторым списком
def delete_zero(numbers):

    catalog = []

    for number in numbers:
        if number != 0:
            catalog.append(number)

    return catalog

print(delete_zero([1,5,7,0,2,0]))

#без списка
def delete_zero_1(numbers):
    i = 0 #индекс элемента списка (его позиция)

    while i < len(numbers):
        if numbers[i] == 0:
            numbers.pop(i) #после удаления все элементы сдвигаются влево
        else:
            i += 1

    return numbers

#удаление всех отрицательных чисел 
#1
def negative_numbers(numbers):

    i = 0

    while i < len(numbers):
        if numbers[i] < 0:
            numbers.pop(i)
        else:
            i += 1

    return numbers
print(negative_numbers([1, -2, 5, -7, -8, 0, 3, 6]))

#2
def negative_numbers_1(numbers):

    catalog = []

    for number in numbers:
        if number >= 0:
            catalog.append(number)

    return catalog

print(negative_numbers_1([1, -2, 5, -7, -8, 0, 3, 6]))

#удаление всех четных чисел
#1
def delete_even(numbers):

    i = 0

    while i < len(numbers):
        if numbers[i] % 2 == 0:
            numbers.pop(i)
        else:
            i += 1

    return numbers
print(delete_even([1, 2, 5, 4, 6, 8, 3]))

#2
def delete_even_1(numbers):

    catalog = []

    for number in numbers:
        if number % 2 != 0:
            catalog.append(number)

    return catalog

print(delete_even_1([1, 2, 5, 4, 6, 8, 3]))


#Напиши функцию, которая перемещает все нули в конец списка, 
#сохраняя порядок остальных элементов.

#left → позиция, куда поставить следующий ненулевой элемент
#right → текущий элемент, который мы просматриваем
#def move_zero(numbers):
    #left = 0 
    #for right in range(len(numbers)): #len(numbers) - число сколько нам нужно пройти - 1 (индекс с нуля)
        #if right[numbers] != 0:
           # numbers[left], numbers[right] == numbers[right], numbers[left]
           # left += 1 
    #return 

#print(move_zero([1, 0, 2, 0, 3]))

#Напиши функцию, которая находит максимальный элемент списка 
#без использования max().
def max_number(numbers):

    max_element = numbers[0]

    for number in numbers:
        if number > max_element:
            max_element = number

    return max_element

print(max_number([1, 4, 5, 6, 2, -1, 10]))

#с использованием функции max()
def max_number_1(numbers):
    return max(numbers)

print(max_number_1([1, 4, 5, 6, 2, -1, 10]))

#Напиши функцию, которая находит второй по величине уникальный 
#элемент списка.
#регение с сортировкой
def second_unique(numbers):

    seen = set()

    for number in numbers:
        if number not in seen:
            seen.add(number)

    sorted_numbers = sorted(seen)

    if len(sorted_numbers) < 2:
        return None
    
    return sorted_numbers[1]

print(second_unique([1, -2, 4, 4, 6, 4, 7, 10, 10]))

#решение с максимумом
def second_unique_1(numbers):

    seen = set()

    for number in numbers:
        if number not in seen:
            seen.add(number)

    if len(seen) < 2:
        return None 

    seen.remove(max(seen))
    max_element = max(seen)

    return max_element

print(second_unique_1([1, -2, 4, 4, 6, 4, 7, 10, 10]))

#Напиши функцию, которая возвращает все повторяющиеся элементы 
#списка без повторения самих дубликатов в результате.
def find_duplicate(numbers):

    seen = set()
    duplicate = []

    for number in numbers:
        if number not in seen:
            seen.add(number)
        elif number not in duplicate:
            duplicate.append(number)

    return duplicate

print(find_duplicate([5,5,5,5]))

#Напиши функцию, которая удаляет дубликаты из списка, сохраняя 
#первоначальный порядок элементов.
def delete_duplicate(numbers):

    catalog = []

    for number in numbers:
        if number not in catalog:
            catalog.append(number)

    return catalog
print(delete_duplicate([1, 2, 4, 5 ,6 , 6, 2, 5]))

def zero_move(numbers):
    left = 0 

    for right in range(len(numbers)):
        if numbers[right] != 0:
            numbers[left], numbers[right] = numbers[left], numbers[right]
            left += 1

    return numbers

#Напиши функцию, которая возвращает сумму всех чётных чисел списка.
def sum_even(numbers):

    summa = 0 

    for number in numbers:
        if number % 2 == 0:
            summa += number 

    return summa

print(sum_even([1, 2, 3, 4, 5, 6]))


def sum_even_1(numbers):

    return sum(number for number in numbers if number % 2 == 0)

print(sum_even_1([1, 2, 3, 4, 5, 6]))
        
#Напиши функцию, которая находит первый положительный элемент списка.
def first_pozitive_number(numbers):

    for number in numbers:
        if number > 0:
            return number

print(first_pozitive_number([-2, 5, 7, -10]))

#Напиши функцию, которая проверяет, отсортирован ли список 
#по возрастанию.
def is_sorted(numbers):

    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False

    return True

print(is_sorted([1, 2, 3, 4]))  # True
print(is_sorted([1, 3, 2, 4]))  # False
print(is_sorted([5, 5, 5]))  # True

#Напиши функцию, которая объединяет два списка, оставляя 
#только уникальные элементы.
def union_elements(numbers_1, numbers_2):

    seen_1 = set()
    seen_2 = set()

    for number_1 in numbers_1:
        if number_1 not in seen_1:
            seen_1.add(number_1)

    for number_2 in numbers_2:
        if number_2 not in seen_2:
            seen_2.add(number_2)

    return seen_1.union(seen_2)

print(union_elements([1, 2, 3 ,4 ,5, 6], [1, 2, 7, 4, 9, 6]))

#без проверки if number_1 not in seen_1 перед добавлением (она не нужна, потому что множество и так хранит уникальные элементы)
def union_elements_1(numbers_1, numbers_2):
    seen_1 = set(numbers_1)
    seen_2 = set(numbers_2)

    return seen_1.union(seen_2) #return set(numbers_1) | set(numbers_2)

print(union_elements_1([1, 2, 3 ,4 ,5, 6], [1, 2, 7, 4, 9, 6]))

#Напиши функцию, которая находит пропущенные числа в 
#последовательности от 1 до N.
def missing_element(numbers, N):

    missing = []

    for i in range(1, N + 1):
        if i not in numbers:
            missing.append(i)

    return missing

print(missing_element([1, 2, 4, 6], 6))

#Напиши функцию, которая проверяет, правильно ли 
#закрываются круглые скобки в строке.
def check_brackets(symbols):

    stack = []

    pairs = {
        ")":"("
    }

    for symbol in symbols:
        if symbol == "(":
            stack.append(symbol)
        else:
            if not stack:
                return False
            
            if stack.pop() != pairs[symbol]:
                return False
        
    return len(stack) == 0

#Напиши функцию, которая проверяет правильность 
#последовательности круглых, квадратных и фигурных скобок.
def check_brackets_1(symbols):

    stack = []

    pair = {
        ")":"(",
        "]":"[",
        "}":"{"
    }
#если мы проверяем только ОДНУ открываюшуюся скобку, то используем ==, если несколько - IN
    for symbol in symbols:
        if symbol in '([{':
            stack.append(symbol)
        else:
            if not stack:
                return False

            if stack.pop() != pair[symbol]:
                return False

    return len(stack) == 0

print(check_brackets_1(")()[]{}"))

