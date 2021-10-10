print("Программа ТаксиСотрудники")
while True:
    try:
        staff = int(input("Введите количетсво сотрудников(от 1 до 1000): "))
        break
    except(ValueError, TypeError):
        print(print('Вы ввели неверное значение'))
taxi = {}
distances = {}
j = 0
g = 0
for i in range(staff):
    g = g + 1
    distances[g] = input("Введиде дистанцию в км : ")
sorted_distances = sorted(distances.items(), key=lambda x: x[1], reverse=True)
for i in range(staff):
    j = j + 1
    taxi[j] = input("Введите тариф такси: ")
sorted_taxi = sorted(taxi.items(), key=lambda x: x[1])
print("Номер сотрудника и его км:")
print(sorted_distances)
print("Номер машины куда должен сесть сотрудник и ее тариф:")
print(sorted_taxi)
