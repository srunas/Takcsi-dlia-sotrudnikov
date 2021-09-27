print("Программа ТаксиСотрудники")
while(1):
    staff = int(input("Введите количетсво сотрудников(от 1 до 1000: "))
    if 1 <= staff <= 1000:
        staffX = []
        n = 0
        for i in range(1, staff+1):
            staffX.append(i)
        tariffs = sorted([int(s) for s in input("Введите через пробел тарифы такси: ").split()])
        distances = sorted([int(s) for s in input("Введиде дистанцию в км (через пробел): ").split()], reverse=True)
        # ПО СУТИ ВЕСЬ СМЫСЛ ПРОГРАММЫ ЗАЛОДЕН В ВЕРХНИХ 3Х СТРОЧКАХ,
        # работают они по принципу сортировки через i и в целом понятно и хорошо работают
        print(sum(t*d for t, d in zip(tariffs, distances)), 'рублей')
        for i in range(len(staffX)):
            print(staffX[i], "Сотрудник/Тариф такси", tariffs[i], 'рублей/Машина №', n + i+1)
    else: print("Вы ввели не верное количество сотрудников, попробуйте еще раз :D")
    # Верхняя строчка чистейшей воды выпендреж так что не обращайте внимание)