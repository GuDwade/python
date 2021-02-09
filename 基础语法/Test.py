class Dog(object):

    def __init__(self,name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳的玩耍 " % self.name)

class XiaoTianDog(Dog):

    def game(self):
        print("%s 飞到天上去玩耍" % self.name)


class Person(object):

    def __init__(self,name):
        self.name = name


    def game_with_dog(self,dog):
        print("%s 和 %s快乐的玩耍 " %(self.name,dog.name))



dog = Dog("旺财")
xiaoming = Person("小明")

xiaoming.game_with_dog(dog)

dog1 = XiaoTianDog("神狗")
xiaoming.game_with_dog(dog1)