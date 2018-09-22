# Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
# Подсчитайте количество слов в тексте
# Замените точки в тексте на восклицательные знаки
# Сохраните результат в файл referat2.txt
from pprint import pprint
import re
with open('referat.txt', 'r', encoding='utf-8') as ref:
    # reading a file
    referat = ref.read()
    length1 = len(referat)
    print(('The text length without editing is: {0}').format(length1))

    # print (content)
    # replacing extra spaces 
    content = re.sub(r'\s+', ' ', referat)
    length2 = len(content)
    print(('The text length is: {0}').format(length2))
    list_of_words = content.replace('.', '!')
    # print(list_of_words)

def count_all_words():
    # replacing paragraph symbols with space and making list
    list_of_words = (content.replace('\n', ' ')).split()
    # pprint (list_of_words)
    # counting elements in list
    number = 0
    for word in list_of_words:
        number+=1
    return number
print ('The number of words in text is: ', count_all_words())

with open('referat2.txt', 'w', encoding='utf-8') as d:
      d.write(list_of_words)