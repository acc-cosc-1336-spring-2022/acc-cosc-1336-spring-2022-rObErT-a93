#HW 9
import class_a

def main():
    roll_dice = class_a.Die()
    user_choice = 'n'
    user_choice = input('Would you like to roll the dice? (y or n): ')
    while user_choice.lower() == 'y':
        roll_dice.roll()
        print(roll_dice)
        user_choice = input('Would you like to roll again?: ')
    while user_choice.lower() == 'n':
        print('Thanks for rolling...')
        quit()
main()