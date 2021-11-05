
# 2

# создадим пустые списки
my_list = [] # список элементов в кубе
new_list = [] # список суммы каждого элемента из my_list
new_list1 = [] # список элементов, делящие на 7
epilog_list = [] # конечный список

# создадим список, состоящий из кубов нечётных чисел от 1 до 1000
for i in range(1, 1001, 2):
    my_list.append(i ** 3)

print(my_list) # посмотрим наш длинный список

# попробуем преобразовать наш список
for i in range(len(my_list)):
    str1 = str(my_list[i])  # распакуем числа из списка
    map_object = map(int, str1) # конвертируем строки в числа

    list_of_int = list(map_object) # разбиваем числа в цифры
    real_num = sum(list_of_int) # суммируем отдельно каждый элемент
    new_list.append(real_num) # и добавим в новый список

    if new_list[i] % 7 == 0: # делаем условие, если сумма элемента списка делится на 7
        new_list1.append(new_list[i]) # то добавим в отдельный список

final_list = [i+17 for i in new_list1] # прибавим к каждому элементу в списке 17

# делаем тоже самое: разбиваем и суммируем каждый элемент из списки final_list
for i in range(len(final_list)):
    str2 = str(final_list[i])
    map_object1 = map(int, str2)

    list_of_int1 = list(map_object1)
    real_num1 = sum(list_of_int1)
    epilog_list.append(real_num1)

print(new_list)
print(new_list1)
print(final_list)
print()
print(epilog_list) # конечный результат













