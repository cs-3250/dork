# -*- coding: utf-8 -*-
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
import textwrap

def __init__(self):

# The quit command
def do_quit(self, arg):
    """Quit the game"""
    return True # this exits the CMD app loop

############################################################################
"""  CANNOT USE!!
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.lexers import Lexer


def repl():
    ''' REPL: Read–Eval–Print Loop '''
    while True:
        user_input = read() #
        stop, output = evaluate(user_input)
        if output:
            print(output)
        if stop:
            exit(0)
            
            
def read():
    '''read user CLI input'''
    #try:
        #return prompt('» ')#,
                      #lexer=SyntaxLexer(),
                      #history=FileHistory('history.log'))
    #except (EOFError, KeyboardInterrupt):  # ctrl+d & ctrl+c respectively
        #return "quit game"


def main(*args):  # main CLI runner for Dork
    '''main function'''
__all__ = ["main"]



from dork.parser import Parser
from dork import actions


# color scheme: https://github.com/chriskempson/tomorrow-theme
STYLES = {
    'subject':              '#f0c674',  # yellow
    'verb':                 '#cc6666',  # red
    'adverb':               '#b294bb',  # purple
    'direct object':        '#81a2be',  # blue
    'indirect object':      '#b5bd68',  # green
    'preposition':          '#969896',  # gray
    'prepositional object': '#de935f'   # orange
}

"""
class SyntaxLexer(Lexer):
    """NLP Lexer for prompt-toolkit using Spacy
        https://python-prompt-toolkit.readthedocs.io/en/latest/pages/reference.html
        https://github.com/prompt-toolkit/python-prompt-toolkit/
            styles/base.py
            styles/defaults.py
    """
    """
    def lex_document(self, document):
        def get_line(lineno):
            line = document.lines[lineno]
            doc = Parser(line)
            return [
                (STYLES[doc.chunks[token]]
                 if token in doc.chunks else '',
                 token.text_with_ws)
                for token in doc]
        return get_line





def evaluate(user_input):
    '''evaluate user CLI input'''
    doc = Parser(user_input)
    # to do: why not just make command a Parser attribute?
    command = doc.resolve_action()
    if command:
        response = getattr(actions, command)(**doc.parameters)
        if isinstance(response, tuple):
            stop_flag, output = response
            return stop_flag, output
        return False, response
    return False, None

def main(*args):  # main CLI runner for Dork
    '''main function'''
    script_name = args[0] if args else '???'
    if "-h" in args or '--help' in args:
        print("usage:", script_name, "[-h]")
    # to do: handle bad arguments
    else:
        repl()
    """