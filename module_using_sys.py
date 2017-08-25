import sys
# 如果为了避免每次都要输入 sys. 可以使用from sys import argv

print('The command line arguments are: ')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')

import os
print(os.getcwd())


# 一般来说应该尽量避免使用from...import语句，而去使用import语句。
# 这是为了避免在你的程序中出现名称冲突，同时也为了使程序更加易读。
from math import sqrt
print("Square root of 16 is", sqrt(16))
