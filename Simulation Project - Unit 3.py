import random

def roll_die():
    return random.randint(1,6)

def roll_until_six():
    rolls = 0
    while True:
        roll = roll_die()
        rolls += 1
        if roll == 6:
            return rolls

total_rolls = 0
trials = 1000

for i in range(trials):
    total_rolls += roll_until_six()

average_rolls = total_rolls/trials
print("On average, it takes", average_rolls, "rolls to get a 6.")