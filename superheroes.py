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
        self.max_block = random.randint(0,(self.max_block))
        return self.max_block
class Weapon(Ability):
    def __init__(self,name,attack_strength):
        self.name = name
        self.attack_strength = attack_strength
    def attack(self):
        return random.randint(self.attack_strength//2,self.attack_strength)

class Hero:
    def __init__(self,name,starting_health=100):
        self.name = name
        self.abilities = []
        self.armors = []
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0
        pass
    def add_ability(self,ability):
        self.abilities.append(ability)
    def add_weapon(self,weapon):
        self.abilities.append(weapon)
    def add_armor(self,armor):
        self.armors.append(armor)
    def attack(self):
        damage = 0
        for ability in self.abilities:
            damage += ability.attack()
        return damage
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
        if len(self.abilities) and len(opponent.abilities) == 0:
            print(self.name+" and "+opponent.name+" had a draw.")
        while (self.current_health > 0 and opponent.current_health > 0):
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
        if self.current_health > 0:
            print(self.name + " wins!")
            self.add_kills(1)
            opponent.add_death(1)
        else:
            print(opponent.name + " wins!")
            self.add_deaths(1)
            opponent.add_death(1)
    def add_kills(self,num_kills):
        self.kills += num_kills
    def add_deaths(self,num_deaths):
        self.deaths += num_deaths

class Team(object):
    def __init__(self,name):
        self.name = name
        self.heroes = []
        self.dead = []
        self.total_kills = 0
        self.total_deaths = 0
        self.alive = True
    def remove_hero(self,name):
        for hero in self.heroes:
            found = False
            if (hero.name == name):
                self.heroes.remove(hero)
                found = True
        if not found:
            return 0
    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)
    def add_hero(self,hero):
        self.heroes.append(hero)
    def attack(self, other_team):
        random.shuffle(self.heroes)
        random.shuffle(other_team.heroes)
        if not self.heroes[0].is_alive():
            self.dead.append(self.heroes.pop(0))
        elif not other_team.heroes[0].is_alive():
            other_team.dead.append(other_team.heroes.pop(0))
    def revive_heroes(self, health=100):
        for _ in range(len(self.dead)):
            self.dead[0].current_health = self.dead[0].starting_health
            self.heroes.append(self.dead[0])
            self.dead.remove(self.dead[0])
    def stats(self):
        for hero in self.heroes:
            print(hero.name+"has a kills/deaths ratio of "+hero.kills+".")

class Arena(object):
    def __init__(self):
        self.team_one = None
        self.team_two = None
    def create_ability(self):
        name = input("Add an ability: ")
        damage = int(input("Add a damage value for the ability: "))
        return Ability(name,damage)
    def create_weapon(self):
        name = input("Add a weapon: ")
        damage = int(input("Add a damage value for the weapon: "))
        return Weapon(name,damage)
    def create_armor(self):
        name = input("Add an armor: ")
        block = int(input("Add a block value: "))
        return Armor(name,block)
    def create_hero(self):
        name = input("Create a hero's name:")
        health = int(input("Add a health value for the hero: "))
        ability = self.create_ability()
        weapon = self.create_weapon()
        new_hero = Hero(name,health)
        new_hero.add_ability(ability)
        new_hero.add_weapon(weapon)
        return new_hero
    def build_team_one(self):
        name = input("Name team 1: ")
        self.team_one = Team(name)
        team_members = int(input("Add a number of team members: "))
        for _ in range(team_members):
            self.team_one.heroes.append(self.create_hero())
    def build_team_two(self):
        name = input("Name team 2: ")
        self.team_two = Team(name)
        team_members = int(input("Add a number of team members: "))
        for _ in range(team_members):
            self.team_two.heroes.append(self.create_hero())
    def team_battle(self):
        self.team_one.attack(self.team_two)
    def show_stats(self):
        team_one_kills = 0
        team_one_deaths = 0
        team_two_kills = 0
        team_two_deaths = 0
        if(len(self.team_two.heroes) == 0):
            print("Team "+self.team_one.name+" wins!")
            print("Survivors: ")
        for hero in self.team_one.heroes:
            print(hero.name)
            team_one_kills += hero.kills
            team_one_deaths += hero.deaths
        for hero in self.team_one.dead:
            team_one_kills += hero.kills
            team_one_deaths += hero.deaths
        else:
            print("Team "+self.team_two.name+" wins!")
            print("Survivors: ")
        for hero in self.team_two.heroes:
            print(hero.name)
            team_two_kills += hero.kills
            team_two_deaths += hero.deaths
        for hero in self.team_two.dead:
            team_two_kills += hero.kills
            team_two_deaths += hero.deaths

        avgOne = team_one_kills
        if team_one_deaths > 0:
            avgOne = avgOne//team_one_deaths

        avgTwo = team_two_kills
        if self.team_two.total_deaths > 0:
            avgTwo = avgTwo//team_two_deaths    
        print("The average K/D ratio of team 1 is: "+str(avgOne))
        print("The average K/D ratio of team 2 is: "+str(avgTwo))
if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
    #hello