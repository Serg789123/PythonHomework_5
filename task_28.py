# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных 
# чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
# 4

def summ(a, b):
    if b == 0:
        return a
    return summ(a, b - 1) + 1 
 
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

print(f"сумма чисел a и b = {summ(a, b)}")