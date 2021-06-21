"""
2.
Задание на закрепление знаний по модулю json. 

Есть файл orders в формате JSON с информацией о заказах. 
Написать скрипт, автоматизирующий его заполнение данными. 

Для этого:
Создать функцию write_order_to_json(), 
в которую передается 5 параметров — товар (item), количество (quantity), 
цена (price), покупатель (buyer), дата (date). 

Функция должна предусматривать запись данных в виде словаря в файл orders.json. 
При записи данных указать величину отступа в 4 пробельных символа;

Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""
import json


data = ["Fridge", "15", "23350", "Mike Johnson", "2021-05-08"]


def write_order_to_json(item, quantity, price, buyer, date):
    dict_data = {
        "item": item,
        "quantity": quantity,
        "price": price,
        "buyer": buyer,
        "date": date,
    }

    with open("orders.json", "w") as f:
        json.dump(dict_data, f, sort_keys=True, indent=4)


write_order_to_json(data[0], data[1], data[2], data[3], data[4])


with open("orders.json") as f:
    print(f.read())
