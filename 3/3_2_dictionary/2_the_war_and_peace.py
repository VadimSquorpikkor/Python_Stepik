# Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой книге.
#
# Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова, разделённые пробелом и
# вывести получившуюся статистику.
#
# Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального слова в этой строке
# число его повторений (без учёта регистра) в формате "слово количество" (см. пример вывода).
# Порядок вывода слов может быть произвольным, каждое уникальное слово должно выводиться только один раз.
#
# Sample Input 1:
# a aa abC aa ac abc bcd a
#
# Sample Output 1:
# ac 1
# a 2
# abc 2
# bcd 1
# aa 2
#
# Sample Input 2:
# a A a
#
# Sample Output 2:
# a 3


def add_to_dictionary(d, s):
    if s in d:
        d[s] = d[s] + 1
    else:
        d[s] = 1


stroke = input().lower()
start = int(0)
dic = {}
for i in range(len(stroke)):
    if stroke[i] == ' ':
        add_to_dictionary(dic, stroke[start: i])
        start = i + 1
add_to_dictionary(dic, stroke[start:])

for key, value in dic.items():
    print(key, value)

#########################################
"""s=[str.upper() for str in input().split()]
for word in set(s) :
        print(word,' ',s.count(word))"""
#########################################
"""c = input().lower().split()
d = {}
for a in c:
    d[a] = c.count(a)
for key, value in d.items():
    print(key, value)"""
#########################################
