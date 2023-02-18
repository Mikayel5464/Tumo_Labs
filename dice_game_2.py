import random


def roll_dice():
    return random.randint(1, 6)


def dice_game():
    dice_1 = roll_dice()
    dice_2 = roll_dice()
    sum_of_dice_1 = dice_1 + dice_2
    print("The sum of dice is {} + {} = {}".format(dice_1, dice_2, sum_of_dice_1))
    
    if sum_of_dice_1 == 7 or sum_of_dice_1 == 11:
        print("You won")
        return
    elif sum_of_dice_1 == 2 or sum_of_dice_1 == 3 or sum_of_dice_1 == 12:
        print("You lose")
        return
    else:
        goal = sum_of_dice_1
        print("Now your goal number is {}".format(goal))
        sum_of_dice_2 = roll_dice() + roll_dice()
        
        while sum_of_dice_2 != goal and sum_of_dice_2 != 7:
            dice_3 = roll_dice()
            dice_4 = roll_dice()
            sum_of_dice_2 = dice_3 + dice_4
            print("The sum of dice is {} + {} = {}".format(dice_3, dice_4, sum_of_dice_2))

        if sum_of_dice_2 == goal:
            print("You won")
        elif sum_of_dice_2 == 7:
            print("You lose")


dice_game()
