# Дополнительная
# Выведите таблицу размером n×n, заполненную числами от 1 до n^2 по спирали, выходящей
# из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):
#
# Sample Input:
#
# 5
#
# Sample Output:
#
# 1 2 3 4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9

n = int(input())
matrix = [[0] * n for i in range(n)]
stopUp = int(n)
stopDown = int(-1)
count = 1
x = 0
y = 0
while count <= n ** 2:
    for x in range(x, stopUp):  # 0-4
        matrix[y][x] = count
        count += 1
    y += 1
    for y in range(y, stopUp):
        matrix[y][x] = count
        count += 1
    x -= 1
    for x in range(x, stopDown, -1):
        matrix[y][x] = count
        count += 1
    y -= 1
    stopDown += 1
    for y in range(y, stopDown, -1):
        matrix[y][x] = count
        count += 1
    x += 1
    stopUp -= 1
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')  # would set end='\t'
    print('')
