import time

vowel = ['A','E','I','O','U','a','e','i','o','u']

print('Let\'s change all the vowels in your name to "oob"s... You know, for fun... #shrugs')
time.sleep(1.5)
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')

def name_mod(first_name, last_name):

    mod_first = ''
    mod_last = ''

    for i in first_name:
        if i in vowel:
            mod_first += 'oob'
        else:
            mod_first += i

    for i in last_name:
        if i in vowel:
            mod_last += 'oob'
        else:
            mod_last += i

    return(f'Modified Name: {mod_first.capitalize()} {mod_last.capitalize()}')

result = name_mod(first_name, last_name)
print(f'Original Name: {first_name} {last_name}\n{result}')
time.sleep(1)
print('\n"Fun..." Extra basic, yet demonstrative, fun...')
time.sleep(2)