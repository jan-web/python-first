food = input("Введите затраты на еду: ")
trans = input("Введите затраты на транспорт: ")
divers = input("Введите затраты на развлечения: ")
total = int(food) + int(trans) + int(divers)
media = total / 3
print(f"Общая сумма", total)
print(f"Средняя сумма", media)