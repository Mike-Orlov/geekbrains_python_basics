"""
Реализовать формирование списка, используя функцию range() и возможности генератора. 
В список должны войти четные числа от 100 до 1000 (включая границы). 
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""

from functools import reduce

def mult(el1, el2):
    """It makes addition for 2 digits"""
    return el1 * el2

# Или gen_list = [el for el in range(100, 1001, 2)]
gen_list = [el for el in range(100, 1001) if el % 2 == 0]
print(reduce(mult, gen_list))