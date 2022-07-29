#通常情况下，求和的函数是这样定义的：

def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
print(calc_sum(1,2,3,4))

#如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
print(lazy_sum(1,2,3,4)) #<function lazy_sum.<locals>.sum at 0x101c6ed90>
print(sum((1,2,3,4)))
#当调用lazy_sum()时，返回的并不是求和结果，而是求和函数；调用函数f时，才真正计算求和的结果；
f = lazy_sum(1, 2, 3, 4)
print(f)
print(f())
##函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。




