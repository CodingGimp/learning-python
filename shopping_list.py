import os

shopping_list = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_to_list(item):
    print_list()
    if len(shopping_list):
        position = input('Where should I add {}?\n'
                         'Press ENTER to add to the end of the list.\n'
                         '> '.format(item))
    else:
        position = 0
    
    try: 
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shopping_list.insert(position-1, item)
    else:
        shopping_list.append(item)
    print_list()
    print('{} has been added. You now have {} items on your shopping list...'.format(item, len(shopping_list)))
    

def show_help():
    clear_screen()
    print('What item would you like to add to your shopping list?')
    print('''
    If you need help, type "Help". 
    If you would like to see what is on your list, type "List".
    If you would like to delete an item from your list, type "Remove".
    If you are done, type "Done".
    ''')

def print_list():
    clear_screen()
    print('=====Shopping List=====')
    index = 1
    for item in shopping_list:
        print('{}. {}'.format(index, item))
        index += 1
    print('=======================')

def remove_item():
    print_list()        
    item_to_remove = input('Which item would you like to remove?\n> ')
    try:
        shopping_list.remove(item_to_remove)
    except ValueError:
        pass
    print_list()

show_help()
while True: 
    new_item = input('> ').title()

    if new_item == 'Done':
        print_list()
        break
    elif new_item == 'List':
        print_list()
        continue
    elif new_item == 'Remove':
        remove_item()
    elif new_item == 'Help':
        show_help()
        continue

    add_to_list(new_item)
