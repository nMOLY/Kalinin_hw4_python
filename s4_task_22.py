# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))

set1 = set()
set2 = set()

print("Введите элементы первого множества:")
for _ in range(n):
    element = int(input())
    set1.add(element)

print("Введите элементы второго множества:")
for _ in range(m):
    element = int(input())
    set2.add(element)

result = sorted(set1.intersection(set2))

print("Элементы, которые встречаются в обоих множествах и отсортированы в порядке возрастания:")
for element in result:
    print(element)