import uuid
import random
import server.constants as constants


class Item:
    def __init__(self):
        # 道具类.以ID操作
        self.category = random.randint(0, len(constants.attribute)-1)
        self.id = uuid.uuid1()

    def get_category(self):
        print("本件道具是：", constants.category[self.category])


class Equipment(Item):
    def __init__(self):
        # 装备类.继承类Item类
        self.category = 0
        self.id = uuid.uuid1()
        self.type = random.randint(0, len(constants.equipments)-1)

    def get_type(self):
        # 打印装备类型
        print(constants.equipments[self.type])

