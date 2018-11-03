import uuid
import random
import server.constants as constants


class Player():
    def __init__(self):
        self.id = str(uuid.uuid1())  # 玩家每个人对应一个不同多id
        self.name = ""  # 玩家昵称.由set_name来定义
        self.level = 1  # 玩家默认等级
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

    def choose_occupation(self, occupation):
        self.occupation = occupation
        print(self.name + '选择职业:' + constants.occupations[occupation])

    def set_name(self,name):
        self.name = name

    def level_up(self):
        old_level = self.level
        self.level += 1

        print(self.name, '升级啦! ', old_level,'-->', self.level)

    def get_all(self):
        print('玩家所有信息:')
        print('id:'+self.id)
        print('level:'+str(self.level))
        print('name:'+self.name)
        print('职业:'+str(self.occupation))
        print('\n')


player = Player()
player.set_name('wsp')
player.level_up()
player.choose_occupation(0)
player.get_all()
