# не решила
#
#
#
# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение —  кортеж вещей.
# Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами.
# Код должен расширяться на любое большее количество друзей.

my_dict = {}
while True:
    print('1 - Добавить друга')
    print('2 - Выход')
    action = input('Введите номер операции: ')
    match action:
        case "1":
            my_dict[input('Введите имя: ')] = tuple(input('Введите наименования вещей через пробел: ').split())
        case "2":
            print("Словарь = ", my_dict)
            my_list = []
            for i in my_dict.values():
                my_list.append(set(i))
            print("Все вещи = ", my_list)
            print("Вещи, которые взяли все друзья: ", *set.intersection(*my_list))
            print("Уникальные вещи, которые есть только у одного друга: ", *set.union(*my_list).difference(set.intersection(*my_list)))
            new_dict = {}
            for key, value in my_dict.items():
                temp = key
                if key!= temp:
                    new_dict[key] = value
            print("Новый словарь", new_dict)
                # if value not in set.intersection(*my_list):
                #     new_dict[key] = set.intersection(*my_list)



            # print("Вещи, которые есть у всех кроме одного, имя: ", set.intersection(*my_list))

            quit()
