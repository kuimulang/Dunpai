# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，所以，我们把Student类改一改：
# class Student(object):
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#     def print_score(self):
#         print('%s: %s' % (self.__name, self.__score))
# 改完后，对于外部代码来说，没什么变动，但是已经无法从外部访问实例变量.__name和实例变量.__score了：
# bart = Student('Bart Simpson', 59)
# print( bart.__name)  #这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。

##但是如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法：
class Student1(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_score(self, score):
        self.__score = score
    def set_name(self, name):
        self.__name = name
bart = Student1('Bart Simpson', 59)
# print(bart.__name) #这种方法是错误的
print(bart.get_name())
bart.set_name('New Name1111')
bart.__name = 'New Name2222' #这种方法是错误的
print(bart.__name)
# 表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量。不信试试：
print(bart.get_name())
