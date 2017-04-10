#  Напишите программу, на вход которой подается одна строка с целыми числами.
#  Программа должна вывести сумму этих чисел.
#
#  Используйте метод split строки.
#
#  Sample Input:
#  4 -1 9 3
#
#  Sample Output:
#  15

""" inputList = [int(x) for x in input().split()]
 print(sum(inputList)) """

print(sum([int(x) for x in input().split()]))
