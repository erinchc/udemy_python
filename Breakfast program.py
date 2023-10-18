name = input('Enter your name: ')
# print('Your name is ' + name)

money = input('Enter your cash amount: ')
hungry = input('Are you hungry? (Y/N) ')

if hungry == 'Y':
    if int(money)>=30:
        print(f'{name}, you should go eat.')
    else:
        print(f'{name} is hungry but might not have enough money to eat.')
elif hungry == 'N':
    if int(money)>=30:
        print(f'{name} has budget but doesn\'t want to eat.')
    else:
        print(f'{name} has no money but is not hungry.')
else:
    print('Please make sure that you enter either Y or N.')