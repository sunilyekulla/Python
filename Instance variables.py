import random

class Enemy:
    def __init__(self,atkl,atkh):
        self.atkl=atkl
        self.atkh=atkh

    def getAtk(self):
        print(self.atkl)

enemy1=Enemy(40, 49)
enemy1.getAtk()

enemy2=Enemy(60, 80)
enemy2.getAtk()

