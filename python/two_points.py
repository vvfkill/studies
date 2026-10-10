text = "hello"

#print(text[0])
#print(text[-1])

#индекс - просто число, которое говорит, где находится элемент

#for i in range(len(text)):
    #print(i)
    #print(text[i])
left = 0 
right = len(text) - 1 #len("hello") = 5 -> последний индекс 4 
text[left] == text[right]

#left += 1 двигаем вправо
#right -= 1 двигаем влево 

#палиндром
def is_palindrom(text):

    left = 0 
    right = len(text) - 1 

    while left < right:

        if text[left] == text[right]:
            left += 1
            right -= 1 
        else:
            return False
        
    return True

print(is_palindrom("level"))

#функция, которая перемещает все 0 в конец списка, 
#сохраняя исходный порядок остальных элементов.

#left → позиция, куда поставить следующий ненулевой элемент
#right → текущий элемент, который мы просматриваем
def move_zero(numbers):
    left = 0 
    for right in range(len(numbers)) #len(numbers) - число сколько нам нужно пройти - 1 (индекс с нуля)
        if right[numbers] != 0:
            numbers[left], numbers[right] == numbers[right], numbers[left]
            left += 1 
    return 

print(move_zero([1, 0, 2, 0, 3]))
#Напиши функцию remove_duplicates, которая получает отсортированный список чисел 
#и удаляет из него повторяющиеся элементы, сохраняя порядок.

def remove_duplicates(numbers):
    left = 0

    for right in range(len(numbers)):
        if numbers[right] != numbers[left]:
            left += 1 #показываем куда нужно поставить уникальное значение
            numbers[left] = numbers[right] #перезаписываем чисто (возьми значение справа и запиши его влево)

    return numbers[:left + 1] #+1 нужен потому что правая граница не включается

#def compress_string(numbers):
#    count = 1


#print(compress_string("aaabbc")) #-> "a3b2c1"



