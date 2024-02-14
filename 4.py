import csv


def generate_promo(*args):
    """функция для генерации промокодов
    args - информация о товаре в следущем формате: Category;product;Date;Price per unit;Count"""
    product, date = args[1].upper(), args[2]
    day, month = date.split('.')[:2]
    promo = product[:2] + day + product[-2:][::-1] + month[::-1]
    return promo

with open('products.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    data = list(reader)[1:]

for i in range(len(data)):
    data[i].append(generate_promo(*data[i]))

with open('product_promo.csv', 'w') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Category', 'product', 'Date', 'Price per unit', 'Count', 'promocode'])
    writer.writerows(data)