class Tool(object):
    count = 0;

    def __init__(self,name):
        self.name = name;

        Tool.count += 1

    @classmethod
    def show_count(cls):
        print("tools类实例个数为%d" % cls.count)

    # 不访问实例属性 何 类属性
    @staticmethod
    def introuduce():
        print("请查看说明书")

tool1 = Tool("榔头")
tool2 = Tool("斧子")

print(Tool.count)
Tool.show_count()
Tool.introuduce()