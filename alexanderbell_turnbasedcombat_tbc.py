'''
Alexander Bell
Oct-17

A module for a turn-based combat game, which pits two characters against each other
'''
import random

class character:
    def __init__(self,name,hitPoints,hitChance,maxDamage,armor):
        self.name = name
        self.hitPoints = hitPoints
        self.hitChance = hitChance
        self.maxDamage = maxDamage
        self.armor = armor

    def printStats(self):
        to_print = [self.hitPoints,self.hitChance,self.maxDamage,self.armor]
        print(self.name)
        print("================")
        for item in to_print:
            print(item)
        print("\n")

    def hit(char1,char2):
        hit = random.randint(1,100)
        if hit <= char2.hitChance:
            damage = random.randint(1,char2.maxDamage)
            damage_dealt = damage - char1.armor

            print(f"{char2.name} hits {char1.name}...")
            print(f"for {damage} hit points")
            print(f"{char1.name}'s armor can reduce damage by {char1.armor} points")

            if damage_dealt > 0:
                return damage_dealt
            else:
                damage_dealt = 0
                return damage_dealt
        else:
            print(f"{char2.name} misses {char1.name}...")
            damage_dealt = 0
            return damage_dealt

    def fight(char1,char2):
        keepGoing = True
        health_char1 = char1.hitPoints
        health_char2 = char2.hitPoints
        while keepGoing:
            new_round = input("\n\npress enter to go to the next round...")
            if keepGoing == True:
                damaged_char1 = character.hit(char1,char2)
                health_char1 -= damaged_char1
                char1.hitPoints = health_char1
                character.printStats(char1)

                if health_char1 <= 0:
                    keepGoing = False
                    print(f"{char2.name} wins!!!")
            if keepGoing == True:
                damaged_char2 = character.hit(char2,char1)
                health_char2 -= damaged_char2
                char2.hitPoints = health_char2
                character.printStats(char2)

                if health_char2 <= 0:
                    keepGoing = False
                    print(f"{char1.name} wins!!!")

     


def main():
    char1 = character("test",8,99,8,2)
    char2 = character("testing",8,1,8,2)

    character.printStats(char1)
    print("\n")
    character.printStats(char2)
    print("\n")

    damage_1 = character.hit(char1,char2)
    print(damage_1)
    
    damage_2 = character.hit(char2,char1)
    print (damage_2)

    character.fight(char1,char2)

if __name__ == "__main__":
	main()

