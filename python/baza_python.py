#Напиши функцию is_even(number), которая принимает целое число и возвращает True,
#если число чётное, и False, если нечётное.
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(4))

#Напиши функцию: count_vowels(s). Она принимает строку и должна вернуть количество гласных букв в ней. 
# Считать гласными: a, e, i, o, u
def count_vowels(s):
    count = 0 
    for letter in s:
        if letter in 'aeiou':
            count += 1 
    return(count)

print(count_vowels('asdfghytree'))

#Напиши функцию: find_max(numbers). Она принимает список целых чисел и возвращает самое большое число из списка.
def find_max(numbers):
    count = numbers[0]
    for number in numbers:
        if number > count:
            count = number         
    return(count)


print(find_max([2,5,6,7]))

#Напиши функцию: ount_occurrences(numbers, target). Она должна посчитать, сколько раз target встречается в списке.
def ount_occurrences(numbers, target):
    count = 0 
    for number in numbers:
        if number == target:
            count += 1
    return(count)
print(ount_occurrences([2,3,4,5,6,6,2,1], 6))

#Напиши функцию: find_min_max(numbers). Она должна вернуть минимальное и максимальное число списка.
def find_min_max(numbers):
    max = [0] #3 #3 #8
    min = [0] #3 #1
    for number in numbers:
        if number > max:
            max = number 
        if number < min:
            min = number
    return(min, max)

print(find_min_max([3,1,8,11,4]))


#Напиши функцию: reverse_string(s). Она должна вернуть строку в обратном порядке.
def reverse_string(s): #пустая строка
    result = "" #пустая строка
    for i in s(len(s) - 1, -1, -1): #-1 потому что 0 мы захватываем, так как это первый символ строки
        result = result + s[i]
    return result
print(reverse_string('list'))


#Напиши функцию: is_palindrome(s). Она должна возвращать True, если строка является палиндромом, и False, если нет.
def is_palindrom(s):
    result = '' 
    for i in range(len(s) - 1, -1, -1):
        result = result + s[i]
    
    if result == s:
        return True
    else:
        return False

#1
def count_positive(numbers):
    count = 0
    for number in numbers:
        if number > 0:
            count += 1
    return(count)

print(count_positive([1, 2, -3, 6, -10, -12]))

#2
def sum_even(numbers):
    total = 0
    for number in numbers:
        if number % 2 == 0:
            total = total + number
    return(total)
print(sum_even([1, 3, -4, 5, -10]))

#3
def find_min(numbers):
    min_total = numbers[0]
    for number in numbers:
        if number < min_total:
            min_total = number
    return(min_total)

print(find_min([12, 5, 7, 1]))

#4
def find_number(numbers, target):
    for number in numbers:
        if number == target:
            return True 
    return False

print(find_number([1, 4, 7, 5, 2], 2))   

#5
def count_negative(numbers):
    count = 0 
    for number in numbers:
        if number < 0:
            count += 1 
    return(count)

print(count_negative([-1, 5, 6, -9, -16]))

#6
def find_max(numbers):
    large_number = numbers[0]
    for number in numbers:
        if large_number < number:
            large_number = number
    return(large_number)
print(find_max([1, 4, 7, 5, 2]))   

#7
def count_letters(s, target):
    count = 0
    for letter in s:
        if letter == target:
            count += 1 
    return(count)
print(count_letters('hello', 'l'))  

#8
def find_first_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            return(number)

print(find_first_even([1, 3, 2, 5, 6]))

#9
def positive_numbers(numbers):
    lists = [] #создание списка
    for number in numbers:
        if number > 0:
            lists.append(number) #добавление элемента в список
    return(lists)
print(positive_numbers([1, -2, 4, -20, -3, 5]))

#10
def count_greater(numbers, target):
    count = 0 
    for number in numbers:
        if number > target:
            count += 1
    return(count)
print(count_greater([1, 4, 5, 8, 10, 7, -1], 3))

#11
def get_event_numbers(numbers):
    list = []
    for number in numbers:
        if number %2 == 0:
            list.append(number)
    return(list)
print(get_event_numbers([1, 4, 5, -3, 6, 8]))

#12 (1)
def find_last_positive_1(numbers):
    for i in range(len(numbers) - 1, - 1, - 1):
        if numbers[i] > 0:
            return(numbers)
        return None
print(find_last_positive_1([1, -2, 5, -3, 7]))

#12 (1)
def find_last_positive_2(numbers):
    positive = 0 
    for number in numbers:
        if number > 0:
            positive = number
    return(positive)
print(find_last_positive_2([1, -2, 5, -3, 7]))

#13
def count_long_words(words):
    count = 0 
    for word in words:
        if len(word) > 5:
            count += 1
    return(count)
print(count_long_words(["cat", "having", "python", "number", "dog"]))


