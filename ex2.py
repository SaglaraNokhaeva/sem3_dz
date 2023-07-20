# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

my_list = input("Введите список повторяющихся элементов через пробел: ").split()
duplicate_list = []
for i in list(set(my_list)):
    if my_list.count(i) >= 2:
        for j in range(my_list.count(i)):
            duplicate_list.append(i)
print("Список без дубликатов: ", *set(my_list))
print("Список с дублирующимися элементами: ", *duplicate_list)