class Fraction():
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
myf = Fraction(3,5)
print(myf) #显示存储在变量中的实际引用（地址本身）
def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n
class Fraction():
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
    def show(self):
        print(self.num,"/",self.den)
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum
myf = Fraction(3,5)
print(myf) #3/5
myf.show() #3 / 5
'''
__str__(self)在以下情况下会被自动调用：
使用 print(obj) 时
使用 str(obj) 时
在 f-string 或格式化字符串中嵌入对象时
'''
print("I ate", myf, "of the pizza") #I ate 3/5 of the pizza
print(myf.__str__()) #3/5
print(str(myf)) #3/5
f1=Fraction(1,4)
f2=Fraction(1,2)
f3=f1+f2
'''
__add__(self)在+会自动调用
'''
print(f3) #3/4
print(f1 == f2) #False
'''
__eq__(self)在==会自动调用
'''
'''
`__lt__` 是 "less than" 的缩写，对应运算符 <。
当你写 obj1 < obj2 时,Python 会自动调用 `obj1.__lt__(obj2)`。
'''
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # 定义 __repr__
    def __repr__(self):
        return f"Coordinate(x={self.x}, y={self.y})"
    # 定义 __str__
    def __str__(self):
        return f"({self.x}, {self.y})"
# 测试
p = Coordinate(3, 4)
print(p)         # 调用 __str__，输出: (3, 4)
print(repr(p))   # 调用 __repr__，输出: Coordinate(x=3, y=4)
'''
__repr__
当你把对象放在**列表(List)或字典(Dict)**里时,Python 默认会调用 __repr__ 而不是 __str__。

points = [Coordinate(1, 2), Coordinate(3, 4)]
# 如果没有 __repr__,这里会打印出 [<__main__.Coordinate object at 0x...>, ...]
# 有了 __repr__,你会看到:
# [Coordinate(x=1, y=2), Coordinate(x=3, y=4)]
print(points)
'''
'''
只要一个类实现了 __iter__ 方法，你就可以对它使用 for...in 循环。
当你写 for item in my_obj: 时,Python 幕后做了两件事：
调用 my_obj.__iter__()。这个方法必须返回一个迭代器(Iterator)对象。
不断调用那个迭代器的 __next__() 方法来获取下一个元素，直到捕获到 StopIteration 异常。
'''
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        # 这里的逻辑很关键：每次开始循环时，我们返回一个新的“执行状态”
        n = self.start
        while n > 0:
            yield n  # yield 会自动让 __iter__ 返回一个迭代器对象
            n -= 1
# 测试
count = Countdown(3)
for num in count:
    print(num)
# 输出:
# 3
# 2
# 1
class Classroom:
    def __init__(self, students):
        self.students = set(students)  # 使用集合，查找速度极快
    def __contains__(self, name):
        # 自定义逻辑：只要名字在列表里，或者名字是“校长”，就返回 True
        if name == "Principal":
            return True
        return name in self.students
# 测试
my_class = Classroom(["Alice", "Bob", "Charlie"])
print("Alice" in my_class)      # 输出: True
print("David" in my_class)      # 输出: False
print("Principal" in my_class)  # 输出: True (即便不在学生列表里)