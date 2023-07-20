# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или
# из документации к языку.

import wikipedia

DUPLICATE = 10

my_str = wikipedia.summary("Python (programming language)").lower()
print("Исходная строка: ", my_str)
my_list = my_str.replace(';',' ').replace(',',' ').replace('.',' ').replace('"',' ').replace(':',' ').replace('!',' ').split()
print("Разбили строку: ", my_list)
new_list = []
for i in my_list:
    if i not in new_list:
        new_list.append(i)
print("Список слов без повторов: ", new_list)
rez = {}
for i in new_list:
    count = my_list.count(i)
    rez[i] = count
print("Словарь слов с количествами повторений: ", rez)
sorted_dict = {}
sorted_keys = sorted(rez, key=rez.get, reverse=True)  # [1, 3, 2]

for _ in sorted_keys:
    sorted_dict[_] = rez[_]

print("Отсортировали словарь: ", sorted_dict)
print("10 самых частых слов: ", *list(sorted_dict.items())[:DUPLICATE])





# print(wikipedia.page("Python (programming language)").content)



