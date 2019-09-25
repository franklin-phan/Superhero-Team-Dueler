import random
class Ability:
    def __init__(self,name,attack_strength):
        self.name = name
        self.max_damage = attack_strength
        pass
    def attack(self):
        self.attack_strength = random.randint(0,100)
        return self.attack_strength
        
if __name__ == "__main__":
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())
