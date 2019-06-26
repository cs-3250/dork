""" basic Dork CLI

-MH 06/22/2019 - 12:27pm #########################################

*** For now *** if you change something, leave a comment of the thought you
are trying to convey so others can understand the same logic.

-Needs to:
    -be able to have a dictionary for parsing.
    -Have a quit function
    -Be able to perform actions and have cardinal directions.
    -Have a REPL.
-Currently needs:
-Object interaction
    -A way for player movement
        -N, S, E, W
    -Game commands
        -Quit
        -Start-Save-Load
Definition of done:
    -Create test cases for actions in REPL
    -Added actions into CLI dictionaries

"""
from dork import gamedictionary
print(gamedictionary)

def evaluate(user_input):
    '''evaluate user CLI input'''
    parsed_input = parser(user_input)
    
    if parsed_input[0] is in gamedictionary.ACTION
        output = ACTION.get(parsed_input[0])
    else:
        default = 'Im Sorry. I didnt understand ' + parsed_input[0]
    return output


def parser(user_input)


def repl():
    ''' REPL: Read–Eval–Print Loop '''
    title = 'hello\n'
    output = title
    while True:
        user_input = input(output)
        if 'quit' in user_input:
            print('You have quit.  Goodbye!')
            break
        else:
            output = evaluate(user_input)

repl()