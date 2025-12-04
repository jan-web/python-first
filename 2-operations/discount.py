fullprice = input("Введите стоимость товара: ")
discount = input("Введите размер скидки: ")
pricediscount = int(fullprice) - (int(fullprice) * int(discount) / 100)
print(f"Цена со скидкой", pricediscount)

