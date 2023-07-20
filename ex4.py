# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.

my_dict = {'water': 2000, 'food': 1000, 'dishes': 300, 'first_aid_kit': 400, 'clothes': 500, 'flashlight': 300}
max_weight = int(input("Введите максимальную грузоподъёмность в граммах: "))
summ_weight = 0

sorted_dict = {}
sorted_keys = sorted(my_dict, key=my_dict.get, reverse=True)  # [1, 3, 2]

for _ in sorted_keys:
    sorted_dict[_] = my_dict[_]

print("Отсортировали по весу: ", sorted_dict)
print("Берём в рюкзак: ")
for key, value in my_dict.items():
    if (summ_weight + value) <= max_weight:
        summ_weight += value
        print(key, " - Итого:", summ_weight)

    else:
        quit()


