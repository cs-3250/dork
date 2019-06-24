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
def gameStart():
    print('#################################################################')
    userInput = input('Hello welcome to the game!\n\nWhat would you like to do? >>>  ')
    evaluate(userInput)
    #print('\nYou ' + userInput)
    
def evaluate(user_input):
    '''evaluate user CLI input'''
    action = user_input
    dictionary = [jump]
        if action() == dictionary():
        print('success!!')
    #doc = Parser(user_input)
    # to do: why not just make command a Parser attribute?
    #command = doc.resolve_action()
    #if command:
    #    response = getattr(actions, command)(**doc.parameters)
    #    if isinstance(response, tuple):
    #        stop_flag, output = response
    #        return stop_flag, output
    #    return False, response
    #return False, None

def repl():
    ''' REPL: Read–Eval–Print Loop '''
    while True:
        user_input = read() #
        stop, output = evaluate(user_input)
        if output:
            print(output)
        if stop:
            exit(0)
            
gameStart()

