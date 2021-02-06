class A:
    def demo(self):
        print("A的方法")

class B:
    def demo(self):
        print("B的方法")

class C(B,A):
    # 尽量避免使用同名方法
    pass


c = C()
c.demo()

#  MRO 方法搜索顺序
print(C.__mro__)

# 新式类  以object为基类
# 经典类  不以object为基类
# python 3.X  默认都是新式类