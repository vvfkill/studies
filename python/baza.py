#Напиши функцию reverse_string(text), 
#которая принимает строку и возвращает её в обратном порядке.
def reverse_string(texts):
    new_line = ""

    for text in range(len(texts) - 1, -1, -1):
        new_line += texts[text]

    return new_line

print(reverse_string("hello")) #-> "olleh"

#Напиши функцию find_duplicates(numbers), 
#которая возвращает все значения, встречающиеся 
#в списке больше одного раза.

def find_duplicates(numbers):
    seen = set()
    duplicate = []

    for number in numbers:
        if number not in seen:
            seen.add(number)
        else:
            duplicate.append(number)
    return duplicate

print(find_duplicates([1, 2, 3, 2, 4, 1]))

#функция возвращает максимальную длину палиндрома, 
#который можно составить из букв строки

def is_palindrom(symbols):
    count = {} #словарь для подсчета букв
    
    for symbol in symbols:
        if symbol in count:
            count[symbol] += 1
        else:
            count[symbol] = 1 #посчитали количество каждого символа

    lenght = 0 #храним длину палиндрома
    has_odd = False #запоминаем встретилось ли нечетное количество символов
    
    for symbol, value in count.items():
        if value % 2 == 0:
            lenght += value
        else:
            lenght += value - 1 
            has_odd = True #обрабатываем количество каждой буквы

    if has_odd:
        lenght += 1

    return lenght

print(is_palindrom("abccccdd"))

def longest_even_part(symbols):
    count = {}

    for symbol in symbols:
        if symbol in count:
            count[symbol] += 1
        else:
            count[symbol] = 1

    length = 0 
    for symbol, value in count.items():
        if value % 2 == 0:
            length += value 
        else:
            length += value - 1

    return length

print(longest_even_part("abccccdd"))

def odd_length(symbols):
    count = {}

    for symbol in symbols:
        if symbol in count:
            count[symbol] += 1
        else:
            count[symbol] = 1

    for symbol, value in count.items():
        if value % 2 != 0:
            return True

    return False
    

##Valid Parentheses##

def valid_parentheses(symbols):
    stack = []

    pairs = { #словарь соответствий
        ")":"(",
        "]":"[",
        "}":"{"
    }

    for symbol in symbols:
        if symbol in "([{":
            stack.append(symbol)
        else:
            if not stack:
                return False
            
            if stack.pop() != pairs[symbol]:
                return False

    return len(stack) == 0

print(valid_parentheses("({[]})"))

def valid_parentheses_1(symbols):
    stack = []

    pairs = {
        ")":"("
    }

    for symbol in symbols:
        if symbol in "(": #in/==
            stack.append(symbol)
        else:
            if not stack:
                return False

            if stack.pop() != pairs[symbol]: #что вытащили последним != что должно закрываться
                return False

    return len(stack) == 0

print(valid_parentheses_1("((())"))

def valid_parentheses_2(symbols):
    stack = []

    pairs_1 = {
        ")":"(",
        "]":"["
    }

    for symbol in symbols:
        if symbol in "([":
            stack.append(symbol)
        else:
            if not stack:
                return False

            if stack.pop() != pairs_1[symbol]:
                return False

    return len(stack) == 0 

print(valid_parentheses_2("((([[[]]])))"))


def purchases_before_ban_1(actions):
    count = 0 

    for action in actions:
        if action["action"] == "purchase":
            count += 1

        if action["action"] == "ban":
            break
            
    return count

print(purchases_before_ban_1([
    {"user": "Anna", "action": "login"},
    {"user": "Anna", "action": "purchase"},
    {"user": "Anna", "action": "purchase"},
    {"user": "Anna", "action": "ban"},
    {"user": "Anna", "action": "purchase"}
]))

def purchases_before_ban_2(actions, user):
    count = 0

    for action in actions:
        if action["user"] != user:
            continue

        if action["action"] == "purchase":
            count += 1

        if action["action"] == "ban":
            break

    return count, user

actions = [
    {"user": "Anna", "action": "purchase"},
    {"user": "Bob", "action": "purchase"},
    {"user": "Anna", "action": "login"},
    {"user": "Anna", "action": "purchase"},
    {"user": "Anna", "action": "ban"},
    {"user": "Bob", "action": "purchase"},
    {"user": "Anna", "action": "purchase"},
]

print(purchases_before_ban_2(actions, "Anna"))
print(purchases_before_ban_2(actions, "Bob"))


def before_ban(actions):
    count = 0

    for action in actions:
        if action["action"] == "purchase":
            count += 1

        if action["action"] == "ban":
            break

    return count

print(before_ban([
                {"action": "purchase"},
                {"action": "purchase"},
                {"action": "ban"}
]))


def before_ban_1(actions, user):
    count = 0 

    for action in actions:

        if action["user"] != user:
            continue 

        if action["action"] == "purchase":
            count += 1

        if action["action"] == "ban":
            break

    return count

print(before_ban_1([
    {"user": "Anna", "action": "purchase"},
    {"user": "Bob", "action": "purchase"},
    {"user": "Anna", "action": "login"},
    {"user": "Bob", "action": "purchase"},
    {"user": "Anna", "action": "purchase"},
    {"user": "Anna", "action": "ban"},
    {"user": "Anna", "action": "purchase"}
], "Anna"))

def last_action(actions, user):
    last = None

    for action in actions:

        if action["user"] == user:
            last = action["action"]

        if action["user"] != user:
            continue

    return last

print(last_action([
    {"user": "Anna", "action": "purchase"},
    {"user": "Bob", "action": "purchase"},
    {"user": "Anna", "action": "login"},
    {"user": "Bob", "action": "purchase"},
    {"user": "Anna", "action": "purchase"},
    {"user": "Anna", "action": "ban"},
    {"user": "Anna", "action": "purchase"}
], "Kate"))

def total_sales(sales):

    totals = {}

    for sale in sales:
        if sale["seller"] not in totals:
            totals[sale["seller"]] = sale["amount"]
        else:
            totals[sale["seller"]] += sale["amount"]

    return totals
        
print(total_sales([
            {"seller": "Anna", "amount": 100},
            {"seller": "Bob", "amount": 200},
            {"seller": "Anna", "amount": 150},
            {"seller": "Kate", "amount": 300},
            {"seller": "Bob", "amount": 100}
]))

#найти топ 1 
def top_sales(sales):

    total = {}

    for sale in sales:
        if sale["seller"] not in total:
            total[sale["seller"]] = sale["amount"]
        else:
            total[sale["seller"]] += sale["amount"]

    sum = 0
    best_seller = None

    for seller, amount in total.items():
        if amount > sum:
            sum = amount
            best_seller = seller

    return best_seller

#найти топ 3

def top_3_seller(sales):

    total = {}

    for sale in sales:
        if sale["seller"] not in total:
            total[sale["seller"]] = sale["amount"]
        else:
            total[sale["seller"]] += sale["amount"]

    top_3_sellers = []

    for i in range(3):
        max_amount = 0
        best_seller = None

        for seller, amount in total.items():
            if amount > max_amount:
                max_amount = amount
                best_seller = seller

        top_3_sellers.append(best_seller)
        del total[best_seller]

    return top_3_sellers

print(top_3_seller([
            {"seller": "Anna", "amount": 100},
            {"seller": "Bob", "amount": 200},
            {"seller": "Anna", "amount": 150},
            {"seller": "Kate", "amount": 300},
            {"seller": "Bob", "amount": 100}
]))  
        

def reverse_string(text):
    result = ""

    for i in range(len(text) - 1, -1, -1):
        result += text[i]

    return result

def find_duplicates(numbers):
    seen = set()
    lists = []

    for number in numbers:
        if number not in seen:
            seen.add(number)
        else:
            lists.append(number)

    return lists

def filter_even(numbers):

    even = []

    for number in numbers:

        if number % 2 == 0:
            even.append(number)

    return even

    

            





        


    


    




