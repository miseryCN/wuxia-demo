"""
这个文件用于初始化玩家的属性。
一 生成玩家名字，uuid，默认等级，经验
    名字：玩家的昵称
    uuid：用于区分玩家，每个玩家仅有唯一的uuid
    默认等级：默认等级为0，等级与经验挂钩
    经验：默认经验为0。

二 生成玩家的战斗属性
战斗属性分为基础属性和五维属性，五维属性层级高于基础属性，五维属性用于加成基础属性。
1 五维属性
    1⃣ 气海：气海加成内功攻击，内功防御。根据不同的职业，加成的系数不同。内功职业加成系数必高于外功职业。
    2⃣ 力道：力道加成外功攻击，外功防御。根据不同的职业，加成的系数不同。外功职业加成系数必高于内功职业。
    3⃣ 洞察：洞察加成命中率，会心率，会心伤害。不同的职业，加成系数不同。
    4⃣ 根骨：根骨加成角色的HP，内功防御，外功防御。不同职业的加成系数不同。
    5⃣ 身法：身法加成角色的会心抗性，格挡率。不同职业的加成系数不同。
2 基础属性
    1⃣ 外功攻击：物理攻击，可以被格挡。如果攻击被格挡，则伤害降低90%。无论是内功职业还是外功职业，都有外功攻击。
    2⃣ 内功攻击：广义上的法术攻击，我们也可以叫做气功。内功攻击无法被格挡。无论是内功职业还是外功职业，都有内功攻击。
    3⃣ 外功防御：这个就很有意思了。外功防御是一个数值。y=1-1/ln(x+e) y表示百分比，x表示数值。
    4⃣ 内功防御：这个也一样很有意思。同外功防御
    5⃣ 格挡：格挡是一个百分比，可以超过100%
    6⃣ 命中：命中是一个百分比，真实命中率 = 你的命中率 - 对方的格挡率
    7⃣ 会心：暴击率。是一个百分比，可以超过100%
    8⃣ 会心抗性：抗暴击率，是一个百分比，可以超过100%
    9⃣ 会心伤害：暴击伤害。暴击数值 = 伤害 * 会心伤害。 是一个百分比，初始值为150%
"""
import uuid
import random
import server.constants as constants
from server.equipment import Equipment


class Player():
    def __init__(self):
        self.id = str(uuid.uuid1())  # 玩家每个人对应一个不同的id
        self.name = ""  # 玩家昵称.由set_name来定义
        self.level = 1  # 玩家默认等级
        self.HP = 0  # 血量
        self.exp = 0  # 玩家经验
        self.attribute = {
            "base": {
                "attack": 0,  # 外攻
                "qi": 0,  # 内攻
                "defend": 0,  # 外攻防御
                "qi_defend": 0,  # 内攻防御
                "block": 0,  # 格挡
                "hit_rate": 0,  # 命中
                "boom": 0,  # 会心
                "boom_multiple": 0,  # 会心伤害
                "boom_defend": 0,  # 会心抗性
            },
            "advance": {
                "qi_hai": 0,
                "li_dao": 0,
                "dong_cha": 0,
                "geng_gu": 0,
                "sheng_fa": 0
            }
        },
        self.occupation = 0  # 职业
        self.bag = []  # 背包
        self.body = []  # 身上穿着

    def choose_occupation(self, occupation):
        # 设置职业
        self.occupation = occupation
        print(self.name + '选择职业:' + constants.occupations[occupation])

    def set_name(self, name):
        # 设置名字
        self.name = name

    def level_up(self):
        # 升1级
        old_level = self.level
        self.level += 1
        print(self.name, '升级啦! ', old_level, '-->', self.level)
        base = self.attribute[0]["base"]
        advance = self.attribute[0]["advance"]
        for key in base:
            base[key] += 1
        for key in advance:
            advance[key] += 1

    def get_all(self):
        # 这是个打印玩家信息的方法
        print('玩家所有信息:')
        print('id:'+self.id)
        print('level:'+str(self.level))
        print('name:'+self.name)
        print('职业:'+str(self.occupation))
        advance = self.attribute[0]["advance"]
        advance_constants = constants.attribute["advance"]
        for key in advance_constants:
            print(advance_constants[key], ':', advance[key])
        base = self.attribute[0]["base"]
        base_constants = constants.attribute["base"]
        for key in base_constants:
            print(base_constants[key], ':', base[key])
        print('\n')

    def add_item(self, item):
        # 添加道具
        self.bag.append(item)

    def remove_item(self, id):
        # 删除道具
        for item,index in self.bag:
            if item["id"] == id:
                self.bag.pop(index)
                break
