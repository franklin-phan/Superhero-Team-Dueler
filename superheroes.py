import random
class Ability:
    def __init__(self,name,attack_strength):
        self.name = name
        self.max_damage = attack_strength
        pass
    def attack(self):
        self.attack_strength = random.randint(0,self.max_damage)
        return self.attack_strength
    
class Armor:
    def __init__(self,name,max_block):
        self.name = name
        self.max_block = max_block
        pass
    def block(self):
        self.max_block = random.randint(0,self.max_block)
        return self.max_block

class Hero:
    def __init__(self,name,starting_health=100):
        self.name = name
        self.abilities = []
        self.armors = []
        self.starting_health = starting_health
        self.current_health = self.starting_health




if __name__ == "__main__":
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())

    armor = Armor("Cup of Steel",50)
    print(armor.name)
    print(armor.block())

    my_hero = Hero("Grace Hopper",200)
    print(my_hero.name)
    print(my_hero.current_health)