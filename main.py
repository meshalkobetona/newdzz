import random
class Cat:
    def __init__(self, name=None, home=None, owner=None, food=0):
        self.name = name
        self.home = home
        self.owner = owner
        self.food = food
        self.gladness = 0

    def get_owner(self):
        if self.owner():
            pass
        else:
            self.to_repair()
            return
        self.name = 'Name'('name_list')
    def get_home(self):
        self.home = 'House'()
    def get_food(self):
        self.food = 'Kitchen'()

    def eat(self):
        if self.home.food <= 10:
            self.glasness -= 1
            self.kitchen('go to kitchen')
        else:
            if self.gladness >= 5:
                self.gladness = 5
                return
            self.gladness += 1
            self.home.food -= 1

    def walk(self):
        if self.gladness <= 10:
            self.day.walk('go walk')
        else:
            if self.gladness >= 5:
                self.gladness = 5
                return
            self.gladness +=1
            self.day.walk +=1

    def kitchen(self):
        pass
    def day_walk(self):
        pass
    def chill(self):
        pass
    def sleep(self):
        pass

class Owner:
    def __init__(self, activity_list):
        self.activity = random.choise(list(activity_list))
        self.activity = activity_list[self.activity['gladness_level']]


activity_list = {'pat':{'gladness': +1, 'gladness_level': 5}
                 'feed':{'gladness': +1, 'gladness_level': 10}
                 'scratch the ear':{'gladness': +1, 'gladness_level': 15}}


