card_list = []


def show_menu():
    """功能菜单"""
    print("*"*50)
    print("欢迎使用名片管理系统")
    print("1.新增名片")
    print("2.显示名片")
    print("3.查询名片")
    print("0.退出系统")
    print("*" * 50)

def create_cards():
    """新增名片"""
    name_str = input("请输入姓名：")
    telephone_str = input("请输入电话：")
    email_str = input("请输入邮箱：")



    card_dict = {"name":name_str,
                 "telephone":telephone_str,
                 "email":email_str}

    card_list.append(card_dict)

    print("添加%s的名片成功"%name_str)

def show_cards():
    """显示名片"""
    if len(card_list) == 0:
        print("当前没有任何名片记录，请先添加名片记录")
        return

    for name in ["姓名","电话","邮箱"]:
        print(name, end="\t\t")
    print()
    print("*"*50)

    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t"%(card_dict["name"],
                                    card_dict["telephone"],
                                    card_dict["email"]))

def search_cards():
    name_str = input("请输入要查找的姓名:")

    for card_dict in card_list:
        if card_dict["name"] == name_str :
            print("姓名\t\t电话\t\t邮箱\t\t")
            print("="*50)
            print("%s\t\t%s\t\t%s\t\t" % (card_dict["name"],
                                          card_dict["telephone"],
                                          card_dict["email"]))
            # TODO 对查找到的名片进行修改和删除
            deal_card(card_dict)
            break
    else:
        print("您要查找的用户%s不存在"%name_str)

def deal_card(card_dict):

    action_str = input("请选择您要执行的操作：【1】修改【2】删除【3】返回")
    if action_str == "1":
        card_dict["name"] = input_judge(card_dict["name"],"请输入姓名（回车不修改）：")
        card_dict["telephone"] = input_judge(card_dict["telephone"],"请输入电话（回车不修改）：")
        card_dict["email"] = input_judge(card_dict["email"],"请输入邮箱（回车不修改）：")
        print("恭喜您修改成功")
    elif action_str == "2":
        card_list.remove(card_dict)
        print("删除成功")

def input_judge(dict_value,message):
    """
        输入修改的信息
    @param dict_value: 原信息
    @param message: 提示语句
    @return: 修改后的信息
    """
    input_str =input(message)
    if len(input_str) > 0:
        return input_str
    else:
        return dict_value
