import random

def play_minigame(bet, purse, start_purse):
    bag = ('green', 'green', 'green', 'green', 'green', 'black', 'red', 'red', 'red', 'white')
    marble = random.choice(bag)
    result = 0

    if marble == 'green':
        result = bet
    elif marble == 'black':
        result = 10 * bet
    elif marble == 'white':
        result = -5 * bet
    else:
        result = -bet

    purse += result
    game_over = purse < 0.5 * start_purse

    return marble, result, purse, game_over