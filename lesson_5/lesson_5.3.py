"""
Создать текстовый файл (не программно), 
построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). 
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. 
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""
result = []

with open('lesson_5.3-example.txt') as staff:
    second_names = []
    salary = []
    # После чтения файла я хочу из каждой строки вытащить фамилию и зарплату в разные списки
    for line in staff:
        line_list = line.split()
        second_names.append(line_list[0])
        salary.append(int(line_list[1]))
# Делаю словарь, чтобы можно было с ним работать под любые цели
staff_dict = dict(zip(second_names, salary))
# В результирующий список извлекаю из словаря фамилии по условию задачи
for name, val in staff_dict.items():
    if val < 20000:
        result.append(name)
print(result)