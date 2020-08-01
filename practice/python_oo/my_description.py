"""用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个"""


# 定义一个喵类
class Cat:
    # 定义名字、颜色属性
    name = "丢丢"
    color = "白色的"
    apperance = "可爱"

    # 定义吃和叫的方法 （def关键字，类中叫方法methord，类外叫函数function）
    def eat(self):
        print("我爱吃小鱼干，下次记得多买点儿呀！")

    def say(self):
        print(f"我好无聊啊，快来陪我玩游戏吧~")


# 实例化猫咪
cat = Cat()
print(f"大家好！我叫{cat.name}，我是{cat.color}，我非常{cat.apperance}！你会喜欢我的~")
cat.eat()
cat.say()

print("———————————————————————————————————————————————————————————————————")


# 定义一个人类,杀阡陌
class ShaQianMo:
    # 定义属性
    gender = "雌雄难辨"
    look = "漂亮帅气"

    # 定义方法meet(),遇到花千骨，柔情似水;遇到白子画，深仇大恨
    def see(self, name):
        if name == "花千骨":
            print("小骨，你来啦~走，姐姐带你去一个好地方！")
        elif name == "白子画":
            print("白子画,你若敢为你门中弟子伤她一分,我便屠你满门!你若敢为天下人损她一毫,我便杀尽天下人！")


# 实例化
sqm = ShaQianMo()
print(f"杀阡陌，长相{sqm.look},时而似温柔的女子，时而像暗黑大魔头，真是{sqm.gender}！")
sqm.see("花千骨")
sqm.see("白子画")

print("———————————————————————————————————————————————————————————————————")


# 定义一首诗
class Poem:
    # 定义诗的名字、作者
    name = "《致橡树》"
    author = "舒婷"

    # 定义方法 favorite()，输出最喜欢的一句
    def favorite(self):
        print(f"最喜欢的诗句是：\n我必须是你近旁的一株木棉，作为树的形象和你站在一起！")


# 实例化
zxs = Poem()
print(f"这首诗的名字是{zxs.name}),作者是{zxs.author}")
zxs.favorite()

print("———————————————————————————————————————————————————————————————————")


# 定义一个手机
class MobilePhone:
    # 定义手机的属性
    name = "小小小粉"
    color = "pink"
    size = "5.0英寸"

    # 定义充电方法charge()
    def charge(self):
        print("我正在充电，请不要和我玩，不然可能炸掉你的手指头！")

    # 定义使用方法use()
    def use(self):
        print("都被你玩坏了，赶紧换一个吧，求放过!")


# 实例化
mobile = MobilePhone()
print(f"我的手机是{mobile.color}，所以我叫它{mobile.name},屏幕大小是{mobile.size}")
mobile.charge()
mobile.use()

print("———————————————————————————————————————————————————————————————————")


# 定义一个Zhaoly(赵丽颖)
class Zhaoly:
    # 定义属性
    height = "165cm"
    weight = "45kg"
    nikname = "赵小刀"
    fans = "萤火虫"
    masterpiece = "《知否知否，应是绿肥红瘦》"

    # 定义方法近期工作recent_work()、常说的话say()
    def recent_work(self):
        print("现担任《中餐厅4》财务总监")

    def say(self):
        print('最喜欢说"菜好贵呀！"')


# 实例化
zly = Zhaoly()
print(f"赵丽颖，身高{zly.height},体重{zly.weight},昵称{zly.nikname},她的粉丝叫{zly.fans}")
zly.recent_work()
zly.say()
