'''
2.
Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
(не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
'''
word1 = b'class'
word2 = b'function'
word3 = b'method'

print(word1, type(word1), len(word1), '\n', word2, type(word2),
      len(word2), '\n', word3, type(word3), len(word3), '\n')
