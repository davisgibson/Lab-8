import random

playerHealth = 100
monsterHealth = 100

print 'A monster approaches! Prepare to fight!'


while (monsterHealth > 0):
    if playerHealth > 0:
        punch = random.randint(1,5)
        sword = random.randint(3,10)
        fireball = random.randint(15,30)
        monsterHit = random.randint(10,20)
        print 'You have ' + str(playerHealth) + ' health, and the monster has ' + str(monsterHealth) + ' health.'
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        print 'Which attack would you like to use?'
        print '1 - Punch. 2 - Sword. 3 - Fireball'
        attack = int(raw_input())
        if attack == 1:
            monsterHealth = monsterHealth - punch
            print 'You hit the monster with your fists. You dealt ' + str(punch) + ' damage.'
        if attack == 2:
            monsterHealth = monsterHealth - sword
            print 'You slashed the monster with your sword. You dealt ' + str(sword) + ' damage.'
        if attack == 3:
            monsterHealth = monsterHealth - fireball
            print 'You launch a ball of fire at the monster. You deal ' + str(fireball) + ' damage.'
        if playerHealth > 0:
            print 'The monster hit you, dealing ' + str(monsterHit) + ' damage.'
            playerHealth = playerHealth - monsterHit
        print '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='
    if playerHealth < 1:
        print 'You have lost! The monster was too strong for your skills!'
        monsterHealth = 0
if playerHealth > 0:
    print 'Congratulations! You have defeated the monster!'