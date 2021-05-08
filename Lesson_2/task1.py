'''
1.

a:
Задание на закрепление знаний по модулю CSV.
Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt, info_3.txt
и формирующий новый «отчетный» файл в формате CSV.

Для этого:
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными,
их открытие и считывание данных. В этой функции из считанных данных необходимо
с помощью регулярных выражений извлечь значения параметров «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список.
Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list.
В этой же функции создать главный список для хранения данных отчета — например,
main_data — и поместить в него названия столбцов отчета в виде списка:
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);

b.
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. 
В этой функции реализовать получение данных через вызов функции get_data(), 
а также сохранение подготовленных данных в соответствующий CSV-файл;
'''
import csv


main_data = [['Изготовитель системы',
              'Название ОС', 'Код продукта', 'Тип системы']]
files = ('info_1.txt', 'info_2.txt', 'info_3.txt')


def get_data():

    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    for i in range(len(files)):
        c = 4
        with open(files[i], encoding='cp1251') as f:
            while c > 0:
                line = f.readline()
                parted_line = (line.split(':')[1].lstrip().rstrip('\n'))
                if line.find('Изготовитель системы') != -1:
                    os_prod_list.append(parted_line)
                    c -= 1
                if line.find('Название ОС') != -1:
                    os_name_list.append(parted_line)
                    c -= 1
                if line.find('Код продукта') != -1:
                    os_code_list.append(parted_line)
                    c -= 1
                if line.find('Тип системы') != -1:
                    os_type_list.append(parted_line)
                    c -= 1

        main_data.append([])
        main_data[i + 1].append(os_prod_list[i])
        main_data[i + 1].append(os_name_list[i])
        main_data[i + 1].append(os_code_list[i])
        main_data[i + 1].append(os_type_list[i])

    return main_data


def write_to_csv(file_to_write):
    with open(file_to_write, 'w') as f:
        f_writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        for row in get_data():
            f_writer.writerow(row)


write_to_csv('main_data.csv')

with open('main_data.csv') as f:
    print(f.read())
