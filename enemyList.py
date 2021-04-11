# This class is used to store the enemy moster lists:
# It contains functions to:
# 1. Retrun a list of monsters based on the difficulty and round

import random


def loadEnemy(difficulty, rounds):
    eFirstMonstNr = 0
    eSecondMonstNr = 0
    eLastMonstNr = 0

    # If player played more than 10 rounds, chose a random enemy (of the last 4 enemies)
    if rounds > 10:
        eRounds = random.randint(7, 10)
    else:
        eRounds = rounds

    # easy
    if difficulty == 0:

        # Enemy in the first round
        if eRounds == 0:
            eFirstMonstNr = 48
            eSecondMonstNr = 50
            eLastMonstNr = 7

        # Enemy in the second Round
        elif eRounds == 1:
            eFirstMonstNr = 49
            eSecondMonstNr = 50
            eLastMonstNr = 7

        elif eRounds == 2:
            eFirstMonstNr = 49
            eSecondMonstNr = 51
            eLastMonstNr = 7

        elif eRounds == 3:
            eFirstMonstNr = 49
            eSecondMonstNr = 51
            eLastMonstNr = 23

        elif eRounds == 4:
            eFirstMonstNr = 53
            eSecondMonstNr = 51
            eLastMonstNr = 23

        elif eRounds == 5:
            eFirstMonstNr = 53
            eSecondMonstNr = 45
            eLastMonstNr = 23

        elif eRounds == 6:
            eFirstMonstNr = 53
            eSecondMonstNr = 45
            eLastMonstNr = 23

        elif eRounds == 7:
            eFirstMonstNr = 19
            eSecondMonstNr = 45
            eLastMonstNr = 23

        elif eRounds == 8:
            eFirstMonstNr = 19
            eSecondMonstNr = 18
            eLastMonstNr = 23

        elif eRounds == 9:
            eFirstMonstNr = 19
            eSecondMonstNr = 18
            eLastMonstNr = 24

        else:
            eFirstMonstNr = 19
            eSecondMonstNr = 18
            eLastMonstNr = 25

    # Medium
    elif difficulty == 1:

        # Enemy in the first round
        if eRounds == 0:
            eFirstMonstNr = 62
            eSecondMonstNr = 5
            eLastMonstNr = 1

        # Enemy in the second Round
        elif eRounds == 1:
            eFirstMonstNr = 63
            eSecondMonstNr = 5
            eLastMonstNr = 1

        elif eRounds == 2:
            eFirstMonstNr = 63
            eSecondMonstNr = 5
            eLastMonstNr = 10

        elif eRounds == 3:
            eFirstMonstNr = 64
            eSecondMonstNr = 5
            eLastMonstNr = 10

        elif eRounds == 4:
            eFirstMonstNr = 64
            eSecondMonstNr = 13
            eLastMonstNr = 10

        elif eRounds == 5:
            eFirstMonstNr = 64
            eSecondMonstNr = 13
            eLastMonstNr = 16

        elif eRounds == 6:
            eFirstMonstNr = 64
            eSecondMonstNr = 19
            eLastMonstNr = 16

        elif eRounds == 7:
            eFirstMonstNr = 21
            eSecondMonstNr = 19
            eLastMonstNr = 16

        elif eRounds == 8:
            eFirstMonstNr = 21
            eSecondMonstNr = 19
            eLastMonstNr = 16

        elif eRounds == 9:
            eFirstMonstNr = 21
            eSecondMonstNr = 19
            eLastMonstNr = 36

        else:
            eFirstMonstNr = 21
            eSecondMonstNr = 42
            eLastMonstNr = 36

    # Hard
    else:

        # Enemy in the first round
        if eRounds == 0:
            eFirstMonstNr = 6
            eSecondMonstNr = 1
            eLastMonstNr = 2

        # Enemy in the second Round
        elif eRounds == 1:
            eFirstMonstNr = 14
            eSecondMonstNr = 1
            eLastMonstNr = 2

        elif eRounds == 2:
            eFirstMonstNr = 20
            eSecondMonstNr = 1
            eLastMonstNr = 2

        elif eRounds == 3:
            eFirstMonstNr = 20
            eSecondMonstNr = 11
            eLastMonstNr = 1

        elif eRounds == 4:
            eFirstMonstNr = 20
            eSecondMonstNr = 11
            eLastMonstNr = 10

        elif eRounds == 5:
            eFirstMonstNr = 10
            eSecondMonstNr = 17
            eLastMonstNr = 20

        elif eRounds == 6:
            eFirstMonstNr = 16
            eSecondMonstNr = 17
            eLastMonstNr = 20

        elif eRounds == 7:
            eFirstMonstNr = 21
            eSecondMonstNr = 17
            eLastMonstNr = 20

        elif eRounds == 8:
            eFirstMonstNr = 61
            eSecondMonstNr = 20
            eLastMonstNr = 68

        elif eRounds == 9:
            eFirstMonstNr = 61
            eSecondMonstNr = 71
            eLastMonstNr = 22

        else:
            eFirstMonstNr = 70
            eSecondMonstNr = 68
            eLastMonstNr = 69

    # Create an array of monster IDs
    enemySelection = [eFirstMonstNr, eSecondMonstNr, eLastMonstNr]

    # return enemy monster list
    return enemySelection
