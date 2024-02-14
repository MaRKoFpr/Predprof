import csv
"""считывание данных таблицы, запись в массив data"""
with open('products.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.reader(file, delimiter=';')
    sells = {}
    for category, product, date, price, count in list(reader)[1:]:
        sells[category] = sells.get(category, {})
        sells[category][product] = sells[category].get(product, 0) + float(count)

"""генерация и запись таблицы"""
hash_table = []
for category, products in sells.items():
    for product, count in products.items():
        hash_table.append([category, count])
hash_table.sort(key=lambda x: x[1])

"""вывод первых 10 строк таблицы"""
for i in range(10):
    print(*hash_table[i])
"""запись таблицы в файл"""
with open('hash_table.csv', 'w') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Category', 'product', 'Date', 'Price per unit', 'Count', 'promocode'])
    writer.writerows(hash_table)

