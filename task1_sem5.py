# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

from encodings import utf_8 
  
with open("str_example.txt", encoding='utf_8') as fin: 
    for line in fin: 
        words = line.split() 
        for word in words: 
            if 'абв' in word: 
                words.remove(word) 
        sentence = " ".join(words) 
        print(sentence)

#Комменты для себя:
# Тип кодирования, которому надо следовать, отображается параметром encoding . Существуют различные типы схем кодирования символов, из которых в Python по умолчанию используется схема UTF-8.
# Источник: https://pythononline.ru/osnovy/encode-decode