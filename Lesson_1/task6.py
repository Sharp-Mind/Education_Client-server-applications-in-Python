'''
6. 
Создать текстовый файл test_file.txt, заполнить его тремя строками: 
«сетевое программирование», «сокет», «декоратор». 
Проверить кодировку файла по умолчанию. 
Принудительно открыть файл в формате Unicode и вывести его содержимое.
'''
import magic


lines = ['сетевое программирование', 'сокет', 'декоратор']


with open('test_file.txt', 'w') as f:
    for line in lines:
        f.write(line + '\n')


blob = open('test_file.txt').read()
m = magic.open(magic.MAGIC_MIME_ENCODING)
m.load()

print(f'Кодировка файла по умолчанию: {m.buffer(blob)}\n')

with open('test_file.txt', 'r', encoding='utf-8') as f:
    data = f.read()

print(data)
