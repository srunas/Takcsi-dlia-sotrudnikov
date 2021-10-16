print("Программа ТаксиСотрудники")
while True:
    try:
        staff = int(input("Введите количетсво сотрудников(от 1 до 1000): "))
        break
    except(ValueError, TypeError):
        print(print('Вы ввели неверное значение'))
taxi = {}
dict_list = []
distances = {}# Тут программа создает пустые словари для дальнейшего добавления в них значений.
j = 0
g = 0
for i in range(staff):
    g = g + 1
    distances[g] = input("Введиде дистанцию в км : ")# Здесь я сделал чтобы программа добовляет значение по ключу в пустой словарь.
sorted_distances = sorted(distances.items(), key=lambda x: x[1])# Ну а тут происходит сортировка по 2му значению в словаре.
for i in range(staff):
    j = j + 1
    taxi[j] = input("Введите тариф такси: ")# Все тоже самое только для трифов такси.
sorted_taxi = sorted(taxi.items(), key=lambda x: x[1], reverse=True)
for i in range(staff):
    my_dict = {item[0]: item[1] for item in zip(sorted_distances, sorted_taxi)}# Объединяю все в один список.
    dict_list.append(my_dict)# Добовляю все в один список.
print("Номер сотрудника/км, Номер машины/тариф")
print('\n'.join(str(el) for el in my_dict.items()),)
# выводится номер сотрудника и его км, а далее номер такси и его тариф