""" basic Dork CLI

-MH 06/22/2019 - 12:27pm #########################################

*** For now *** if you change something, leave a comment of the thought you
are trying to convey so others can understand the same logic. 

-Needs to:
    -be able to have a dictionary for parsing.
    -Have a quit functionno
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
import gamedictionary


def gameStart():
    print('#################################################################')
    userInput = input(
        'Hello welcome to the game!\n\nWhat would you like to do? >>>  ')
   # evaluate(userInput)
    #print('\nYou ' + userInput)


def evaluate(user_input):
    '''evaluate user CLI input'''
    action = user_input
<<<<<<< HEAD
    if action is "north":
        print(gamedictionary.movement['north'])
    # if user_input not in dictionary :
     #   return 'Success ' + dictionary[user_input]

=======
    dictionary = {
        'jump' : 'You have jumped!\n >>',
        'north' : 'You went norh!\n >>',
        'south' : 'You went south!\n >>',
        'east' : 'You went east!\n >>',
        'west' : 'You went west!\n >>',
        'climb' : 'You cant climb yet...\n >>',
        'take' : 'You cant take anything yet...\n >>',
        }
    if user_input in dictionary :
        return 'Success ' + dictionary[user_input]
    else :
        return 'Sorry, I dont know that one...\n >>'
    
>>>>>>> 0c4e8417b761f717e8f6f071107f446ed87d05ed
    #doc = Parser(user_input)
    # to do: why not just make command a Parser attribute?
    #command = doc.resolve_action()
    # if command:
    #    response = getattr(actions, command)(**doc.parameters)
    #    if isinstance(response, tuple):
    #        stop_flag, output = response
    #        return stop_flag, output
    #    return False, response
    # return False, None


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

# repl()


gameStart()
