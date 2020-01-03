"""
Спортсмен занимается ежедневными пробежками. 
В первый день его результат составил a километров. 
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. 
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. 
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22

Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""

day_a_res = int(input('Result in day A: '))
day_b_res = int(input('Target result in day B: '))
i = 1

while day_a_res < day_b_res:
    print(f'{i}-й день: {day_a_res:.2f}')
    i +=1
    day_a_res *= 1.1
    
print(f'Ответ: на {i}-й день спортсмен достиг результата - не менее {day_b_res} км')
    