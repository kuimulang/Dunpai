# 切片用途：取一个list或tuple的部分元素是非常常见的操作

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 笨方法：
print(L[0])
r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)
# 切片做法
print(L[0:3]) # 取前3个
print(L[:3])  #如果第一个索引是0，还可以省略：
print(L[1:3]) #从索引1开始，取出2个元素出来
# Python支持L[-1]取倒数第一个元素；倒数第一个元素的索引是-1
print(L[-2:])
print(L[-2:-1])

L = list(range(100))
print(L[:10])  #前10个
print(L[-10:]) #后10个
print(L[10:20]) #前11-20个数
print(L[:10:2])  #前10个数，每两个取一个
print(L[::5]) #所有数，每5个取一个
print(L[:]) #只写[:]就可以原样复制一个list

#tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple
print((0, 1, 2, 3, 4, 5)[:3])
print('ABCDEFG'[:3])
print('ABCDEFG'[::2])