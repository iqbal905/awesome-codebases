import random

def get_int_input(prompt):
    """Get an integer input from the user with error handling."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter an integer.")

# Define Variables
numLives = 10           # number of player's lives remaining
mNumLives = 12          # number of monster's lives remaining

diceOptions = [1, 2, 3, 4, 5, 6]

# Define weapons array with increasing strength
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

combatStrength = get_int_input("Enter your combat Strength: ")
mCombatStrength = get_int_input("Enter the monster's combat Strength: ")

# Roll dice for weapon selection
weaponRoll = random.choice(diceOptions)
print(f"You rolled a {weaponRoll} for your weapon.")

# Add weapon roll to hero's combat strength
combatStrength += weaponRoll

# Use weaponRoll as an index into the weapons array
selectedWeapon = weapons[weaponRoll - 1]
print(f"Your weapon is: {selectedWeapon}")

# Define weapon strength messages
if weaponRoll <= 2:
    print("You rolled a weak weapon, friend.")
elif weaponRoll <= 4:
    print("Your weapon is meh.")
else:
    print("Nice weapon, friend!")

# Check if weapon is not a Fist
if selectedWeapon != "Fist":
    print("Thank goodness you didn't roll the Fist...")

# Roll for health points
input("Roll the dice for your health points (Press enter)")
healthPoints = random.choice(diceOptions)
print("You rolled " + str(healthPoints) + " health points")

input("Roll the dice for the monster's health points (Press enter)")
mHealthPoints = random.choice(diceOptions)
print("You rolled " + str(mHealthPoints) + " health points for the monster")

# Healing potion roll
input("Roll the dice to see if you find a healing potion (Press enter)")
healingPotion = random.choice([0, 1])
print("Have you found a healing potion?: " + str(bool(healingPotion)))

# Continue game logic...
print("You meet the monster. FIGHT!!")
input("You strike first (Press enter)")

print(f"Your {selectedWeapon} ({combatStrength}) ---> Monster ({mHealthPoints})")
if combatStrength >= mHealthPoints:
    mHealthPoints = 0
    print("You've killed the monster")
else:
    mHealthPoints -= combatStrength
    print("You've reduced the monster's health to: " + str(mHealthPoints))

    print("The monster strikes!!!")
    print(f"Monster's Claw ({mCombatStrength}) ---> You ({healthPoints})")
    if mCombatStrength >= healthPoints:
        healthPoints = 0
        print("You're dead")
    else:
        healthPoints -= mCombatStrength
        print("The monster has reduced your health to: " + str(healthPoints))
