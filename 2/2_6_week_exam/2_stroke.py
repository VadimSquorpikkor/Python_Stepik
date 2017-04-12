# Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
# (число повторяется столько раз, чему равно). На вход программе передаётся положительное целое
# число n — столько элементов последовательности должна отобразить программа. На выходе
# ожидается последовательность чисел, записанных через пробел в одну строку.
#
# Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.
#
# Sample Input:
# 7
#
# Sample Output:
# 1 2 2 3 3 3 4

n = int(input())
# n = int(15)
x = int(1)
stroke = ''
length = int(0)
while n > 0:
    length = x
    while length > 0 and n > 0:
        stroke += str(x) + ' '
        length -= 1
        n -= 1
    x += 1
print(stroke)


"""x = int(input())
lst = []
for k in range(x+1):
    b = [k]
    lst+= b * k
print(' '.join(str(i) for i in lst[:x]))
"""