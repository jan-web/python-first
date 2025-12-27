category = input("Введите категорию ")
match category:
    case 'напиток':
        beverege = input("Введите напиток ")
        match beverege:
            case 'чай':
                print("Чай стоит 5 рублей")
            case 'кофе':
                print("Кофе стоит 10 рублей")
            case 'сок':
                print("Сок стоит 15 рублей")
            case _:
                print("Такого напитка нет")
    case 'суп':
        soup = input("Введите суп ")
        match soup:
            case 'борщ':
                print("Борщ стоит 25 рублей")
            case 'щи':
                print("Щи стоят 30 рублей")
            case 'суп-пюре':
                print("Суп-пюре стоит 35 рублей")
            case _:
                print("Такого блюда нет")
    case 'десерт':
        desert = input("Введите десерт ")
        match desert:
            case 'торт':
                print("торт стоит 25 рублей")
            case 'мороженое':
                print("мороженое стоят 30 рублей")
            case 'фрукты':
                print("фрукты стоит 35 рублей")
            case _:
                print("Такого блюда нет")
    case _:
        print("Такой категории нет")


