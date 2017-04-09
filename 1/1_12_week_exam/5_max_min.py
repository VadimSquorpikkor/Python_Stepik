# Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на консоль
# в три строки сначала максимальное, потом минимальное, после чего оставшееся число.
#
# На ввод могут подаваться и повторяющиеся числа.
#
# Sample Input 1:
# 8
# 2
# 14
#
# Sample Output 1:
# 14
# 2
# 8
#
# Sample Input 2:
# 23
# 23
# 21
#
# Sample Output 2:
# 23
# 21
# 23

maxNum = int(input())
temp = int(input())
if temp > maxNum:
    minNum = maxNum
    maxNum = temp
else:
    minNum = temp
temp = int(input())
if temp > maxNum:
    midNum = maxNum
    maxNum = temp
elif temp < minNum:
    midNum = minNum
    minNum = temp
else:
    midNum = temp
print(maxNum)
print(minNum)
print(midNum)
