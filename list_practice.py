roster = []

answer = input('Would you like to add a player to the list? Type "Y" or "N". ').lower()

while answer == 'y':
    player_name = input('Enter the name of the player to add to the roster: ')
    roster.append(player_name)
    answer = input('Would you like to add a player to the list? Type "Y" or "N". ').lower()

print('There are', len(roster), 'players on the team.')

player_number = 1
for player in roster:
    print('Player', player_number, ':', player)
    player_number += 1

keeper = int(input('Please select the goalkeeper by selecting the player number. (1-{}) '.format(len(roster))))

print('Great!!! The goalkeeper for the game will be {}.'.format(roster[keeper - 1]))

