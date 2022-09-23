# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
# 要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：
print(list(range(1, 11)))

#如果要生成[1x1, 2x2, 3x3, ..., 10x10]
# 用循环的方式
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)
# 列表生成式则可以用一行语句代替循环生成上面的list
print([x * x for x in range(1, 11)])
#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
print([x * x for x in range(1, 11) if x % 2 == 0])
#还可以使用两层循环，可以生成全排列：
print([m + n for m in 'ABC' for n in 'XYZ'])

#列出当前目录下的所有文件和目录名
import os # 导入os模块
print([d for d in os.listdir('..')])  # os.listdir可以列出文件和目录

# 循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, '=', v)
#列表生成式也可以使用两个变量来生成list
print( [k + '=' + v for k, v in d.items()])


#把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])


#使用列表生成式的时候，if...else的用
print([x for x in range(1, 11) if x % 2 == 0])
print([x if x % 2 == 0 else -x for x in range(1, 11)])
#在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else。