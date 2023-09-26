"""
Computes the scores for Yahtzee, a dice game by Milton Bradley.

Author: Frankie Benedetto
Version: 11/08/22
Honor Code:
"""

ONES = 1

TWOS = 2

THREES = 3

FOURS = 4

FIVES = 5

SIXES = 6

THREE_OF_A_KIND = 9

FOUR_OF_A_KIND = 10

FULL_HOUSE = 11

SMALL_STRAIGHT = 12

LARGE_STRAIGHT = 13

YAHTZEE = 14

CHANCE = 15


def add_values(dice):
    """Adds the values of the five dice in the list.

    Args:
        dice(list): list of 5 int dice values.
        
    Returns:
        (int):added value of the dice (index 0 to 4)
    """
    value = dice[0] + dice[1] + dice[2] + dice[3] + dice[4]
    # Write the rest of this function(you do not need to use loops, can just add the
    # the five indexed elements in the dice list.
    return value


def calculate_score(dice, category):
    """Score calculation for the given turn.

    Args:
        dice(list):list of 5 dice values.
        category(int):category selected by the player

    Returns:
        score(int):number of points, or 0 if N/A
    """
    # Write a decision statement to evaluate the score for each category.
    # Cases that require more than several lines of code should be done
    # in separate methods below. Each case should set the value of the
    # score variable, so that you will have only one return statement.
    # boring score stuff, this easy
    score = 0
    y = len(dice) 
    if category == ONES:
        score = dice.count(ONES) * ONES
    if category == TWOS:
        score = dice.count(TWOS) * TWOS
    if category == THREES:
        score = dice.count(THREES) * THREES
    if category == FOURS:
        score = dice.count(FOURS) * FOURS
    if category == FIVES:
        score = dice.count(FIVES) * FIVES
    if category == SIXES:
        score = dice.count(SIXES) * SIXES
    
    # Poker stuff, this not easy 
    if category == THREE_OF_A_KIND:
        for i in range(0, y):
            if dice.count(dice[i]) >= 3:
                score = sum(dice)
        
    if category == FOUR_OF_A_KIND:
        for i in range(0, y):
            if dice.count(dice[i]) >= 4:
                score = sum(dice)
        
    if category == FULL_HOUSE:
        dice.sort()
        if (len(set(dice))) != 2:
            return False
        elif dice[0] != dice[3] or dice[1] != dice[4]:
            score = 25
  
    if category == SMALL_STRAIGHT:
        if 1 in dice and 2 in dice and 3 in dice and 4 in dice:
            score = 30
        elif 2 in dice and 3 in dice and 4 in dice and 5 in dice:
            score = 30
        elif 3 in dice and 4 in dice and 5 in dice and 6 in dice:
            score = 30 
        
    if category == LARGE_STRAIGHT:
        if 1 in dice and 2 in dice and 3 in dice and 4 in dice and 5 in dice:
            score = 40
        elif 2 in dice and 3 in dice and 4 in dice and 5 in dice and 6 in dice:
            score = 40
        
    if category == YAHTZEE:
        for i in range(0, y):
            if 5 == dice.count(dice[0]):
                score = 50
        
    if category == CHANCE:
        score = sum(dice)
        
    return score
