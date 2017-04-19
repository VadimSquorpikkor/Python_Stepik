# Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
# Первое слово в тексте последнего файла: "We".
#
# Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
#
# Все файлы располагаются в каталоге по адресу:
# https://stepic.org/media/attachments/course67/3.6.3/
#
# Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.

import requests

url = 'https://stepic.org/media/attachments/course67/3.6.3/'
goto = url + '699991.txt'
count = 1
file_name = requests.get(goto).text
while file_name[0] != 'W':
    count += 1
    print(file_name)
    goto = url + file_name
    file_name = requests.get(goto).text
print(file_name)
print(count)

"""We are the champions, my friends,
And we'll keep on fighting 'til the end.
We are the champions.
We are the champions.
No time for losers
'Cause we are the champions of the world.
"""
