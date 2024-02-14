import csv

with open('products.csv', 'r', encoding='utf-8-sig') as file:
    """sells словарь со словарями,
     каждый из которых содержит информацию о кол-ве проданных товаров данной категории"""
    reader = csv.reader(file, delimiter=';')
    sells = {}
    for category, product, date, price, count in list(reader)[1:]:
        sells[category] = sells.get(category, {})
        sells[category][product] = sells[category].get(product, 0) + float(count)

category = input()

while category != 'молоко':
    """поиск товара с наименьшим кол-вом продаж и его вывод, либо вывод о неудачном поиске"""
    if category in sells.keys():
        product, count = min(sells[category].items(), key=lambda x: x[1])
        print(f'В категории: {category} товар: {product} был куплен {count} раз')
    else:
        print('Такой категории не существует в нашей БД')
    category = input()