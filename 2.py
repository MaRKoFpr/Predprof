import csv
"""считывание данных таблицы, запись в массив data"""
with open('products.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.reader(file, delimiter=';')
    data = list(reader)[1:]

"""сортировка по категориям и ценам"""
for i in range(1, len(data)):
    while i != 0:
        if data[i][0] < data[i - 1][0]:
            data[i], data[i - 1] = data[i - 1], data[i]
        elif data[i][0] == data[i - 1][0] and data[i][3] > data[i - 1][3]:
            data[i], data[i - 1] = data[i - 1], data[i]
        i -= 1

"""получение информации о самом дорогом товаре в первой категории"""
category = data[0][0]
product = data[0][1]
price = data[0][3]

print(f'В категории: {category} самый дорогой товар: {product} его цена за единицу товара составляет {price}')