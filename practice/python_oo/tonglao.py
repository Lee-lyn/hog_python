"""
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
see_people方法，需要传入一个name参数，
如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”
fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。
需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造
"""


# 定义一个天山童姥类 ，类名为TongLao
class TongLao:
    # 构造方法，定义童姥属性，血量hp，武力值power（通过传入的参数得到）
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power

    # 定义see_people方法，传入一个name参数
    def see_people(self, name):
        # 传入”WYZ”（无崖子），则打印，“师弟！！！！”
        if name == "无崖子":
            print("师弟！！！！")
        # 传入“李秋水”，打印“呸，贱人”
        elif name == "李秋水":
            print("呸，贱人！")
        # 传入“丁春秋”，打印“叛徒！我杀了你”
        elif name == "丁春秋":
            print("叛徒！我要杀了你！")

    # 定义fight_zms方法（天山折梅手），调用此方法会将自己的武力值提升10倍，血量缩减2倍。
    # 传入敌人的血量en_hp，武力值en_power
    def fight_zms(self, en_hp, en_power):
        hp = self.hp / 2 - en_power
        en_hp = en_hp - self.power * 10
        # 打斗一局，比较胜负
        if hp < en_hp:
            print("你给我等着，终会有一天你会败在我的脚下！")
        elif hp > en_hp:
            print("这一天终于到来了，哈哈哈哈哈！哈哈哈哈哈！")
        else:
            raise Exception("哼！小子功夫不错嘛！继续，看我不把你打得落花流水，跪地求饶！")


# 实例化
tl = TongLao(2000, 1000)
tl.see_people("丁春秋")
tl.fight_zms(1000, 2000)
