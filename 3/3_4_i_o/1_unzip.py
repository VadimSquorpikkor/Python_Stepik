# На прошлой неделе мы сжимали строки, используя кодирование повторов. Теперь нашей задачей будет восстановление
# исходной строки обратно.
#
# Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования
# повторов, и производит обратную операцию, получая исходный текст.
#
# Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
#
# В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.
#
# Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия "Start Quiz" у вас появляется
# ссылка "download your dataset". Используйте эту ссылку для того, чтобы загрузить файл со входными данными к себе
# на компьютер. Запустите вашу программу, используя этот файл в качестве входных данных. Выходной файл, который
# при этом у вас получится, надо отправить в качестве ответа на эту задачу.
#
# Sample Input:
# a3b4c2e10b1
#
# Sample Output:
# aaabbbbcceeeeeeeeeeb
#
# У вас есть неограниченное число попыток.
# Время одной попытки: 5 mins


with open('file.txt') as in_file:
    stroke = in_file.readline().strip()

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
num = '0'
out = ''
let = ''
for s in stroke:
    if s in numbers:
        num += s
    else:
        out += let * int(num)
        let = s
        num = '0'
out += let * int(num)
print(out)

with open('file2.txt', 'w') as out_file:
    out_file.write(out)

#####################################################
# import re
# print(''.join([i[0] for i in re.findall(r'\w\d+', input()) for j in range(int(i[1:]))]))