#Напиши функцию, которая 
#принимает строку и возвращает её в обратном порядке.

#решение со списком
def reverse_stroka(symbols):

    stroka = []

    for i in range(len(symbols) - 1, -1, -1):
        stroka.append(symbols[i])

    return stroka

print(reverse_stroka("asdfgh"))

#решение со строкой
def reverse_stroka_1(symbols):

    stroka = ""

    for i in range(len(symbols) - 1, -1, -1):
        stroka += symbols[i]

    return stroka

print(reverse_stroka_1("asdfgh"))

#Напиши функцию, 
#которая считает количество символов в строке без использования len().

def character_count(symbols):

    count = 0 

    for symbol in symbols:
        count += 1

    return count

print(character_count("qwertyuiop"))