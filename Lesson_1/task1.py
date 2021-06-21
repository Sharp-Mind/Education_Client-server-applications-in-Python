# enc_str = 'Кодировка'

# enc_str_bytes = enc_str.encode('utf-8')

# print(enc_str_bytes)

# dec_str_bytes = b'\xd0\x9a\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xba\xd0\xb0'

# print(dec_str_bytes.decode('utf-8'))

'''
1.
Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате 
и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode 
также проверить тип и содержимое переменных.
'''

word1 = 'разработка'
word2 = 'сокет'
word3 = 'декоратор'

print(word1, type(word1), len(word1), '\n', word2, type(word2),
      len(word2), '\n', word3, type(word3), len(word3), '\n')

word1_unicode = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
word2_unicode = '\u0441\u043e\u043a\u0435\u0442'
word3_unicode = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'

print(word1_unicode, type(word1_unicode), len(word1_unicode), '\n', word2_unicode, type(
    word2_unicode), len(word2_unicode), '\n', word3_unicode, type(word3_unicode), len(word3_unicode))
