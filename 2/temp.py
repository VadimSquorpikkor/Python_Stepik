# res = [(x + 2) ** 2 for x in range(4, 13, 5) if x % 3 != 0]
# for i in res:
#     print(i)
# print(res)
##############
# import math
#
# print(math.pi)

import requests

r = requests.get('http://example.com')
print(r.text)



