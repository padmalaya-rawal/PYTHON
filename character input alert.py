name = input("Enter your name: ")

if len(name) > 25:
    print(f'''The maximum character limit is 25.
Entered number of characters: {len(name)}''')
elif len(name) < 2:
    print(f'''Minimum character limit is 2.
Entered number of characters: {len(name)}''')
else:
    print(f'''character limit looks good. 
Entered number of characters: {len(name)}''')