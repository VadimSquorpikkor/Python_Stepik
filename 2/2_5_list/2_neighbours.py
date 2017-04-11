# Напишите программу, на вход которой подаётся список чисел одной строкой.
# Программа должна для каждого элемента этого списка вывести сумму двух его соседей. Для элементов списка,
# являющихся крайними, одним из соседей считается элемент, находящий на противоположном конце этого списка.
# Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).
#
# Если на вход пришло только одно число, надо вывести его же.
#
# Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.
#
# Sample Input 1:
# 1 3 5 6 10
#
# Sample Output 1:
# 13 6 9 15 7
#
# Sample Input 2:
# 10
#
# Sample Output 2:
# 10

"""res = [int(x) for x in input().split()]
stroke = ''
if len(res) == 1:
    stroke = str(res[0])
else:
    res.append(res[0])
    res.insert(0, res[-2])
    for x in range(1, len(res) - 1):
        stroke += str(res[x - 1] + res[x + 1]) + ' '
print(stroke)"""


res = [int(x) for x in input().split()]
stroke = ''
if len(res) == 1:
    stroke = str(res[0])
else:
    for x in range(0, len(res)):
        stroke += str(res[x - 1] + res[x - len(res) + 1]) + ' '
print(stroke)
