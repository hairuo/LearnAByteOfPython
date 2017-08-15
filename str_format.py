age = 20
name = 'Swaroop'

# 采用format方法
print('{0} was {1} years old when he wrote this book' .format(name, age))
print('{1} was {0} years old when he wrote this book' .format(name, age))
print('{} was {} years old when he wrote this book' .format(name, age))
print(name+"was "+str(age)+ " years old when he wrote this book") #这样写太麻烦，因而推荐format
print('why is {0} playing with that python?'.format(name))
print('why is {} playing with that python?'.format(name))

# 对于浮点数 ‘0.333’保留小数点(.)后三位
print('{0:.3f}'.format(1.0/3))
# 使用下划线
# 使用(^)定义 '__hello__' 字符串长度为11
print('{0:_^11}'.format('hello'))
# 基于关键词输出 'Swaroop wrote aA Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

# 使用end防止打印过程出现换行符
print('a', end='')
print('b\n')
# 通过end指定空格结尾
print('a', end=' ')
print('b', end=' ')
print('c')

