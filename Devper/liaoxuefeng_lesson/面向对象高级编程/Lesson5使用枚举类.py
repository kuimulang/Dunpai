from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():  # value属性则是自动赋给成员的int常量
    print(name, '=>', member, ',', member.value)


#如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
from enum import Enum, unique
@unique  #@unique装饰器可以帮助我们检查保证没有重复值。
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
day1 = Weekday.Mon
print(day1)
print(day1.value)
print(Weekday.Mon.value)
for name, member in Weekday.__members__.items():
   print(name, '=>', member)
# 可见，既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量。