class Player:
    name = ''
    health = 100
    hitpower = 10

    def attack(self,obj):
        if obj.health <= 0:
            print(obj.name+" is Dead")
            print(self.name+" saved the Village")
        else:
            obj.health -= self.hitpower
            print("%s were attacked, health: %d" %(obj.name, obj.health))


class Hero(Player):
    health = 200
    hitpower = 20

class Villian(Player):
    health = 150
    hitpower = 25

murali = Hero()
murali.name = "Minnal Murali"

shibu = Villian()
shibu.name = "Shibu"

murali.attack(shibu)
murali.attack(shibu)
murali.attack(shibu)
murali.attack(shibu)
murali.attack(shibu)
murali.attack(shibu)
murali.attack(shibu)
murali.attack(shibu)
murali.attack(shibu)