'''
Alexander Bell
Oct-17

A turn-based combat game where two characters fight to the death based on their stats
'''
import random
import alexanderbell_turnbasedcombat_tbc as tbc


def main():
    '''
    char_stats: 0=name,1=hitPoints,2=hitChance,3=maxDamage,4=armor
    '''
    char1_stats = ["Jar Jar Binks",70,37,12,2]
    char2_stats = ["Kermit the Frog",45,80,15,6]

    char1 = tbc.character(char1_stats[0],char1_stats[1],char1_stats[2],char1_stats[3],char1_stats[4])
    char2 = tbc.character(char2_stats[0],char2_stats[1],char2_stats[2],char2_stats[3],char2_stats[4])

    char1.printStats()
    char2.printStats()

    tbc.character.fight(char1,char2)


if __name__ == "__main__":
	main()



