# dict - словарь 
counts = {}

def new_dict(numbers):
    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1
    return(counts)
print(new_dict([2, 5, 2, 5, 7, 3, 2]))

#set - уникальное множество 
numbers = [1, 2, 3, 2, 1]
duplicate = []

seen = set() #создаем пустой - seen = {}

for number in numbers:
    if number in seen:
        duplicate.append(number)
    else:
        seen.add(number)

#counts.items() - возвращает специальный объект, содержащи пары "ключ - значение"
counts = {
    "cat": 3,
    "dog": 2,
    "bird": 1
}
for key, value in counts.items():
     print(key, value)

#дубликаты
def find_duplicates(numbers):
    seen = set()
    duplicate = []

    for number in numbers:
        if number in seen:
            if number not in duplicate:
                duplicate.append(numbers)
        else:
            seen.add(number)
print(find_duplicates([1, 2, 3, 2, 4, 1, 5]))

def find_duplicates_2(numbers):
    counts = {} #словарь
    duplicate = []

    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1

    for number, count in  counts.items():
        if count > 1:
            duplicate.append(number)

    return duplicate
print(find_duplicates_2([1, 2, 3, 2, 4, 1, 5]))

#two sum
def two_sum_1(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i, j]
    return None
print(two_sum_1([2, 7, 11, 15], 9))

def two_sum_2(numbers, target):
    seen = {}
    for i, number in enumerate(numbers): #enumerate позволяет вернуть пары (индекс эл. и сам эл.)
        needed = target - number 
        if needed in seen:
            return [seen[needed], i]
        seen[number] = i
    return None
print(two_sum_2([2, 7, 11, 15], 9))

##########################################

#1
def has_duplicates(numbers):
    seen = set()

    for number in numbers:
        if number not in seen:
            seen.add(number)
        else:
            return True
    return False
print(has_duplicates([2, 3, 4, 5]))

#2
def unique_elements(numbers):
    seen = set()
    result = []
    for number in numbers:
        if number not in seen:
            seen.add(number)
            result.append(number)
    return result
print(unique_elements([2, 2, 1, 3, 1, 4]))

#3
def find_duplicates(numbers):
    seen = set()
    duplicate = []
    for number in numbers:
        if number not in seen:
            seen.add(number)
        else:
            duplicate.append(number)
    return duplicate
print(find_duplicates([2, 2, 1, 3, 1, 4]))

 #4
def count_elements(numbers):
    counts = {}
    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1
    return counts
print(count_elements([1, 2, 2, 3, 1, 2]))

#5
def most_frequent(numbers):
    counts = {}
    max_count = 0
    result = None
    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1

    for number, count in counts.items():
        if count > max_count:
            max_count = count 
            result = number
    return result
print(most_frequent([1, 2, 2, 3, 2, 1]))

#6
def count_unique(numbers):
    seen = set()
    amount = 0 
    for number in numbers:
        if number not in seen:
            seen.add(number)
    amount = len(seen)
    return (seen, amount)
print(count_unique([1, 2, 2, 3, 3, 3]))
        
#6.1
def find_first_duplicate_1(numbers):
    seen = set()
    first_duplicate = 0
    for number in numbers:
        if number not in seen:
            seen.add(number)
        else:
            first_duplicate = number
            break

    return first_duplicate

#6.2
def find_first_duplicate_2(numbers):
    seen = set()
    for number in numbers:
        if number in seen:
            return number

        seen.add(number)
    return None

#6.3
def find_missing_number(numbers):
    for number in range(1, max(numbers) + 1):
        if number not in numbers:
            return number
    return None
print(find_missing_number([1, 2, 3, 5])) 

#7
def find_missing_number_1(numbers):
    counts = []
    for number in range(1, max(numbers) + 1):
        if number not in numbers:
            counts.append(number)
    return counts
print(find_missing_number_1([1, 2, 3, 5, 7, 10])) 

#8
def non_repeating_number(numbers):
    count = {}
    roster = []
    for number in numbers:
        if number in count:
            count[number] += 1
        else:
            count[number] = 1

    for number, value in count.items():
        if value == 1:
            roster.append(number)
    return roster 

#9
print(non_repeating_number([2, 3, 5, 6, 6, 1]))

def second_largest(numbers):
    seen = set()

    for number in numbers:
        if number not in seen:
            seen.add(number)

    if len(seen) < 2:
        return None

    seen.remove(max(seen))
    return max(seen)

print(second_largest([5, 3, 1, 5, 2]))

#10
def merge_unique(numbers_1, numbers_2):
    seen = set()
    result = []

    for number_1 in numbers_1:
        if number_1 not in seen:
            seen.add(number_1)
            result.append(number_1)

    for number_2 in numbers_2:
        if number_2 not in seen:
            seen.add(number_2)
            result.append(number_2)

    return result
print(merge_unique([1, 2, 3, 3],[6, 7, 8]))

#операции set - unioun, intersection
def merge_unique_1(numbers_1, numbers_2):
    seen1 = set()
    seen2 = set()

    for number_1 in numbers_1:
        if number_1 not in seen1:
            seen1.add(number_1)

    for number_2 in numbers_2:
        if number_2 not in seen2:
            seen2.add(number_2)

    #return seen1.union(seen2) #есть в первом или во втором
    return seen1.intersection(seen2) #оставить элементы и в 1 и во 2
print(merge_unique_1([1, 2, 3, 3, 4, 8],
                     [2, 7, 8, 4, 3, 1]))

#11
def world_frequent(text):
    say = {}
    words = text.split()

    for word in words:
        if word in say:
            say[word] += 1 
        else:
            say[word] = 1

    return say

print(world_frequent("cat dog burd cat cat cat"))

#12
def most_frequent_word(text):
    say = {}
    words = text.split()

    for word in words:
        if word in say:
            say[word] += 1
        else:
            say[word] = 1

    max_value = 0
    result = None
    for word, value in say.items():
        if value > max_value:
            max_value = value
            result = word

    return result
print(most_frequent_word("cat dog bird cat cat dog"))

#13
def first_unique_word(text):
    say = {}
    words = text.split()

    for word in words:
        if word in say:
            say[word] += 1
        else:
            say[word] = 1

    for word, value in say.items():
        if value == 1:
            return word

    return None
print(first_unique_word("cat dog bird cat cat fish dog"))

#14
def firs_unique_char(symbols):
    say = {}

    for symbol in symbols:
        if symbol in say:
            say[symbol] += 1
        else:
            say[symbol] = 1

    for symbol, value in say.items():
        if value == 1:
            return symbol

    return None

print (firs_unique_char("swiss"))

#15
def is_anagramm(firs, second):
    glossary_1 = {}
    glossary_2 = {}

    for symbol in firs:
        if symbol in glossary_1:
            glossary_1[symbol] += 1
        else:
            glossary_1[symbol] = 1

    for symbol in second:
            if symbol in glossary_2:
                glossary_2[symbol] += 1
            else:
                glossary_2[symbol] = 1

    if glossary_1 == glossary_2: #return glossary_1 == glossary_2
        return True
    else:
        return False

print(is_anagramm("listen", "silent"))

#16
def is_anagramm_1(first, second):
    dictionary_1 = {}
    dictionary_2 = {}

    first = first.lower().replace(" ", "")
    second = second.lower().replace(" ", "")

    for symbol in first:
        if symbol in dictionary_1:
            dictionary_1[symbol] += 1
        else:
            dictionary_1[symbol] = 1

    for symbol in second:
        if symbol in dictionary_2:
            dictionary_2[symbol] += 1
        else:
            dictionary_2[symbol] = 1

    return dictionary_1 == dictionary_2
    
print(is_anagramm_1("School Master", "The Classroom")) 

#17
def count_vowels(text):
    count = 0 
    for symbol in text:
        if symbol in 'aeiou':
            count += 1
    return count
print(count_vowels("hello"))

