# НЕ РАБОТАЕТ
with open('2_file.txt') as in_file:
    stroke = in_file.read().strip().lower().split()

out = str(max(stroke)) + ' ' + str(stroke.count(max(stroke)))

with open('2_file_out_2.txt', 'w') as out_file:
    out_file.write(out)
