print("Программа ТаксиСотрудники")
taxi = {}
dict_list = []
distances = {}  # Тут программа создает пустые словари для дальнейшего добавления в них значений.
j = 0
g = 0
while True:
    try:
        staff = int(input("Введите количество сотрудников(от 1 до 1000): "))
        break
    except(ValueError, TypeError):
        print(print('Вы ввели неверное значение'))
if 1 <= staff <= 1000:
    for i in range(staff):
        g = g + 1
        while True:
            try:
                distances[g] = int(input("Введите дистанцию в км : ")) # Здесь я сделал чтобы программа добовляет значение по ключу в пустой словарь.
                break
            except(ValueError, TypeError):
                print(print('Вы ввели неверное значение'))
    sorted_distances = sorted(distances.items(), key=lambda x: x[1]) # Ну а тут происходит сортировка по 2му значению в словаре.
    for i in range(staff):
        j = j + 1
        while True:
            try:
                taxi[j] = int(input("Введите тариф такси: ")) # Все тоже самое только для тарифов такси.
                break
            except(ValueError, TypeError):
                print(print('Вы ввели неверное значение'))
    sorted_taxi = sorted(taxi.items(), key=lambda x: x[1], reverse=True)
    for i in range(staff):
        my_dict = {item[0]: item[1] for item in zip(sorted_distances, sorted_taxi)} # Объединяю все в один список.
        dict_list.append(my_dict) # Добавляю все в один список.
    print("Номер сотрудника/км, Номер машины/тариф")
    print('\n'.join(str(el) for el in sorted(my_dict.items())),)
    # выводится номер сотрудника и его км, а далее номер такси и его тариф
else:
    print("Вы ввели не верную цифру попробуйте еще раз")
