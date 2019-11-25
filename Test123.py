items = {'Daggers': 0, 'BluePotions': 0, 'GoldenFeathers': 0, 'Manuscripts': 0}
abilities = {'fly': 0, ' stealth': 0}

choice = input("You enter a basement and see few items on the floor. What do you want to pick up: a dagger, a mushroom or a sword? ").lower()
if choice == 'dagger':
    items['Daggers'] += 1
    print("You have " + str(items['Daggers']) + " dagger(s).")
else:
    print('Sorry boss, it\'s impossible')
choice = input("As you have a dagger, you can open a chest now. Do you want to do it?").lower()
if choice in ('y', 'yes'):
    items['Daggers'] -= 1
    print('You did it but your blade has cracked. Now you have just as ' + str(items['Daggers']) + ' daggers.')
else:
    print('Ok then, chest, keep your secrets.')



