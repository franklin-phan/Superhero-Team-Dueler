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
        self.current_health = starting_health
        pass
    def add_ability(self,ability):
        self.abilities.append(ability)
    def attack(self):
        damage = 0
        for ability in self.abilities:
            damage += ability.attack()
        return damage
    def add_armor(self,armor):
        self.armors.append(armor)
    def defend(self):
        defense = 0
        for armor in self.armors:
            defense += armor.block()
        return defense
    def take_damage(self, damage):
        take_damage= damage - self.defend()
        self.current_health -= take_damage
    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False
    def fight(self,opponent):
        while (self.current_health > 0 and opponent.current_health > 0):
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
        if self.current_health > 0:
            print(self.name + " wins!")
        else:
            print(opponent.name + " wins!")

if __name__ == "__main__":

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)