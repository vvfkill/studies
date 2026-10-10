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


