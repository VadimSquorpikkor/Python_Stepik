students = ['Ivan', 'Masha', 'Sasha']
students += ['Olga']
students += 'Olga'       # Похожие команды,
students.append('Olga')  # но работают по-разному
print(len(students))
for i in students:
    print(i)

# 9
# Ivan
# Masha
# Sasha
# Olga
# O
# l
# g
# a
# Olga
