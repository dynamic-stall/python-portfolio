"""
A fun script that converts vowels in a user's name to 'oob'.
Takes user input for first and last names and outputs both the original
and modified versions of the full name.

Created: [30-Nov-2024]
Author: [dynamic-stall@github]
"""

import time

vowel = ['A','E','I','O','U','a','e','i','o','u']

def name_mod(first_name, last_name):

    """
    Converts all vowels in a given first and last name to 'oob'.
    
    Args:
        first_name (str): The first name to be modified
        last_name (str): The last name to be modified
        
    Returns:
        str: A formatted string containing both the modified first and last names,
             with the first letter of each name capitalized.
             Format: "Modified Name: [modified_first] [modified_last]"
    
    Example:
        >>> name_mod("John", "Smith")
        "Modified Name: Joobhn Smoobth"
    """

    mod_first = ''
    mod_last = ''

    for i in first_name:
        if i in vowel:
            mod_first += 'oob'
        else:
            mod_first += i

    for j in last_name:
        if j in vowel:
            mod_last += 'oob'
        else:
            mod_last += j

    return f'Modified Name: {mod_first.capitalize()} {mod_last.capitalize()}'

print('Let\'s change all the vowels in your name to "oob"s... You know, for fun... #shrugs')
time.sleep(1.5)

first = input('What is your first name? ')
last = input('What is your last name? ')

result = name_mod(first, last)

print('\n*Drumroll*')
time.sleep(2)
print(f'\nOriginal Name: {first} {last}\n{result}')
time.sleep(1)
print('\n"Fun..." Extra basic, yet demonstrative, fun...')
time.sleep(2)
