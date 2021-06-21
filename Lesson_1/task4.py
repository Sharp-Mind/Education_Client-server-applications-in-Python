'''
4.
Преобразовать слова «разработка», «администрирование», «protocol», «standard» 
из строкового представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).
'''

str1 = 'разработка'
str2 = 'администрирование'
str3 = 'protocol'
str4 = 'standard'

str1_enc = str1.encode('utf-8')
str2_enc = str2.encode('utf-8')
str3_enc = str3.encode('utf-8')
str4_enc = str4.encode('utf-8')

print(str1_enc, str2_enc, str3_enc, str4_enc)

str1_dec = str1_enc.decode('utf-8')
str2_dec = str2_enc.decode('utf-8')
str3_dec = str3_enc.decode('utf-8')
str4_dec = str4_enc.decode('utf-8')

print(str1_dec, str2_dec, str3_dec, str4_dec)
