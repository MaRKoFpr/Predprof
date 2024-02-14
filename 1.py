import csv

"""считывание данных таблицы, запись в массив data"""
with open('products.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.reader(file, delimiter=';')
    data = list(reader)[1:]

""""total_sneks - переменная для записи общей суммы продаж снеков"""
total_sneks = 0
for i in range(len(data)):
    """подсчёт стоимости кажной продажи, дозапись ее в массив data"""
    _count = float(data[i][4])
    price = float(data[i][3])
    total = _count * price
    data[i].append(total)

    if data[i][0] == 'Закуски':
        total_sneks += total
print(total_sneks)

"""создание и заполнение файла products_new.csv информацией из массива data"""
with open('products_new.csv', 'w') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Category', 'product', 'Date', 'Price per unit', 'Count', 'total'])
    writer.writerows(data)

