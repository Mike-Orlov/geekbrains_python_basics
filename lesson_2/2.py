"""
Для списка реализовать обмен значений соседних элементов, 
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. 
При нечетном количестве элементов последний сохранить на своем месте. 
Для заполнения списка элементов необходимо использовать функцию input().
"""

# Создаем пустой лист
my_list = []

# Собираем значения листа, пока пользователь не скажет стоп-слово
while True:
    elem = input('Input next element or type "quit" to stop: ')
    if elem == 'quit':
        break
    my_list.append(elem)

# Если лист слишком маленький, то нам не интересно
if len(my_list) < 2:
    print('Your list is too short')
    
else:
    for i in range(len(my_list)):
        # Цикл while нужен, т.к. если лист нечетный, то срабатывает ошибка когда счетчик доходит
        # до последнего элемента. Он не может в этом случае получить значение my_list[i + 1]
        while i < (len(my_list) - 1):
            if i % 2 != 0:
                break
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
            break

    print(my_list)