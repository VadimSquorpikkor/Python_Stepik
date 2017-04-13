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

n = int(5)
matrix = [[0]*n for i in range(n)]
print(matrix)
startX = int(0)
startY = int(0)
stopX = int(n)
stopY = int(n)
stepX = int(1)
stepY = int(1)
count = 1
x = 0
y = 0
while True:
    for y in range(startY, stopY, stepY):
        matrix[x][y] = count
        count += 1
    stepY = -1
    startY = stopX - 1
    stopY = startX + 1


print(matrix)
