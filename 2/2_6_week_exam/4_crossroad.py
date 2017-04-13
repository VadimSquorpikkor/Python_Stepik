# Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк,
# заканчивающихся строкой, содержащей только строку "end" (без кавычек)
#
# Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме
# элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний
# элемент находится с противоположной стороны матрицы.
#
# В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
#
# Sample Input 1:
#
# 9 5 3
# 0 7 -1
# -5 2 9
# end
#
# Sample Output 1:
#
# 3 21 22
# 10 6 19
# 20 16 -1
#
# Sample Input 2:
#
# 1
# end
#
# Sample Output 2:
#
# 4

"""# inputMatrix = []
# inputMatrix.append([int(x) for x in input().split()])
# inputMatrix = [[9,5,3],[0,7,-1],[-5,2,9]]
inStr = str(input())
stroke = ''
# inputMatrix = [1, 2, 3, 4, 5]
# stroke = ''.join(str(x) for x in inputMatrix)
while inStr != 'end':
    stroke += inStr + ' '
    inStr = str(input())
# stroke = [int(x) for x in ]
print(stroke)"""

"""outStroke = []
a = 0
b = 0
stroke = []
inStr = str(input())
while inStr != 'end':
    b += 1
    temp = [int(x) for x in inStr.split()]
    a = int(len(temp))
    stroke += temp
    inStr = str(input())

# stroke = [4, 1, 3, 2]
for i in range(a * b):
    outStroke += [int(stroke[i - 1]) + int(stroke[i + 1 - a * b]) + int(stroke[i - a]) + int(stroke[i - a * b + a])]
for i in range(0, a * b, a):
    for j in range(i, i + a):
        print(outStroke[j], end=' ')
    print('')
print(stroke)
print(outStroke)
print(stroke[-1])
print(a)
print(b)"""

outStroke = []
a = 0
b = 0
stroke = []
inStr = str(input())
while inStr != 'end':
    b += 1
    temp = [int(x) for x in inStr.split()]
    a = int(len(temp))
    stroke.append(temp)
    inStr = str(input())

# stroke = [4, 1, 3, 2]
for i in range(b):
    outStroke += []
    for j in range(a):
        # outStroke[i] += [int(stroke[i][j - 1]) + int(stroke[i][j - a + 1]) + int(stroke[i - 1][j]) + int(stroke[i - b + 1][j])]
        outStroke[i] += [3]
for i in range(0, a * b, a):
    for j in range(i, i + a):
        print(outStroke[j], end=' ')
    print('')

