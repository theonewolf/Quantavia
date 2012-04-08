#!/usr/bin/env python

import random
from sys import stdin

mage_spells = {
                'f' : [10, '%s cast fireball on %s!'],
                'w' : [20, '%s cast whirlwind on %s!']
              }

classes = {
            'm' : ['Mage', 'Wielders of powerful secret arcane knowledge.',
                   mage_spells],
          }

def lookup_class(lookup):
   return classes[lookup] 

def print_action(src, target, action):
    print action[1] % (src, target)

if __name__ == '__main__':
    dummyAttack = 5
    input1 = ""
    input2 = ""
    input3 = ""
    dummyHealth = 25
    werewolfHealth = 50
    minotaurHealth = 100
    playerHealth = 150
    random.seed() # seeds from current sys time
    fire = random.randint(2,6)
    strike = random.randint(2,6) 
    shoot = random.randint(2,6)
    crit = random.randint(2,12) 
    claw = random.randint(2,8)
    smash = random.randint(4,12)
    print 'Welcome to Gladiator.'
    print 'You have three attacks: strike, fireball (magic), and a crossbow.'
    print 'You type m for fireball, s for strike, and r for your ranged ' +\
          'attack.'
    print 'Basic Training: attack the target dummy.'

    while True:
        if crit == 3:
            fire = fire + 5
        elif crit == 7:
            shoot = shoot + 5
        elif crit == 7:
            strike = strike + 5

        input1 = stdin.readline().strip()
        
        if input1 == 'm':
            print 'The air burns as you cast your fireball.'
            dummyHealth = dummyHealth - fire
            print 'Dummy hp: %d' % (dummyHealth)
        elif input1 == 's':
            print 'You strike the dummy with your sword.'
            dummyHealth = dummyHealth - strike
            print 'Dummy hp: %d' % (dummyHealth)
        elif input1 == "r": 
            print 'Your arrow flies into the target dummy.'
            dummyHealth = dummyHealth - strike
            print 'Dummy hp: %d' % (dummyHealth)
        
        if dummyHealth <= 0:
            print 'Excellent you now know how combat works.'
            print 'You have passed basic training, now prepare for the next' +\
                  'round.'
            break

        if playerHealth <= 0:
            print 'You died to the dummy. Is that even possible!?!?!'
            exit(0)

    print 'A werewolf enters the room.'

    while True:
        if crit == 5:
            claw = claw + 3

        input2 = stdin.readline().strip()

        if input2 == 'm':
            print 'The air burns as you cast your fireball.'
            werewolfHealth = werewolfHealth - fire
            print 'Werewolf hp: %d' % (werewolfHealth)
            playerHealth = playerHealth - claw
            print 'The werewolf claws you!'
            print 'Player hp: %d' % (playerHealth)
        elif input2 == 's':
            print 'You strike the werewolf with your blade!'
            werewolfHealth = werewolfHealth - strike
            print 'Werewolf hp: %d' % (werewolfHealth)
            playerHealth = playerHealth - claw
            print 'The werewolf bites you!'
            print 'Player hp: %d' % (playerHealth)
        elif input2 == 'r':
            print 'Your arrow flies into the Werewolf\'s chest.'
            werewolfHealth = werewolfHealth - fire
            print 'Werewolf hp: %d' % (werewolfHealth)
            playerHealth = playerHealth - claw
            print 'The werewolf claws you!'
            print 'Player hp: %d' % (playerHealth)

        if werewolfHealth <= 0:
            print 'The werewolf roars in pain before falling to the ground ' +\
                  'dead.'
            print 'Congratulations, only one last challenge awaits you.'
            break

        if playerHealth <= 0:
            print 'You died. HAHAHAHA NOOB!!!'
            exit(0)

    print 'You are now level 2!!!'
    fire = fire + 2
    strike = strike + 2
    shoot = shoot + 2
    playerHealth = playerHealth + 25
    print 'A minotaur smashes the door down.'

    while True:
        if crit == 10:
            smash = smash + 5

        input2 = stdin.readline().strip()

        if input2 == 'm':
            print 'The air turns to smoke as you cast your fireball.'
            minotaurHealth = minotaurHealth - fire
            print 'Minotaur hp: %d' % (minotaurHealth)
            playerHealth = playerHealth - smash
            print 'The Minotaur smashes you!'
            print 'Player hp: %d' % (playerHealth)
        elif input2 == 's':
            print 'You stab the minotaur with the blade.'
            minotaurHealth = minotaurHealth - strike
            print 'Minotaur hp: %d' % (minotaurHealth)
            playerHealth = playerHealth - smash
            print 'The Minotaur punches you!'
            print 'Player hp: %d' % (playerHealth)
        elif input2 == 'r': 
            print 'Your arrow flies into the target dummy.'
            minotaurHealth = minotaurHealth - strike
            print 'Minotaur hp: %d' % (minotaurHealth)
            playerHealth = playerHealth - smash
            print 'The Minotaur throws you across the room!'
            print 'Player hp: %d' % (playerHealth)

        if playerHealth <= 0:
            print 'You died. Lol'
            exit(0)

        if minotaurHealth <= 0:
            print 'The minotaur roars for the last time.'
            print 'You enter the town of Goldshire.'
            break
