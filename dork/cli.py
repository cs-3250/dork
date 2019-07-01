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
from dork import gamedictionary as gd

__all__ = ["main", "evaluate", "parser", "repl"]


def evaluate(user_input):
    '''using gamedictionary, provide appropriate command'''
    words = parser(user_input)
    response = 'Im Sorry. I didnt understand what you said.'
    if len(words) == 1:
        response = gd.ACTION.get(words[0], response)
    elif len(words) == 2:
        if words[0] not in gd.ACTION:
            return response
        if words[1] not in gd.ACTION.get(words[0]):
            return response
        response = gd.ACTION.get(words[0]).get(words[1])
    return response


def parser(user_input):
    '''break input into separate words'''
    if not user_input:
        parsed_string = " "

#add a second word and make it say something like that is not in our list.  
#And then that delgates to what word is wrong.  
#Once parser is done it should be able to say that were good or ....else:
        parsed_string = user_input.split() 
        """ sudo code:
        if first item in word is go, movement or pick then 
                and not second item:
                if met say 'I dont understand'
                catch what happens in the parser if it needs app
                more words and they you have more words to provide 
            
                cant pass back and cant quit out 
            
                can add elements before sending it output.  
                Won't need print statements"""
            
    return parsed_string


def repl():
    ''' REPL: Read–Eval–Print Loop '''
    output = '*This is a title screen*\n'
    while True:
        user_input = input(output)
        if 'quit' in user_input:
            print('You have quit.  Goodbye!')
            break
        else:
            output = evaluate(user_input)


def main():
    ''' main to dork '''
    repl()


if __name__ == "__main__":
    repl()
