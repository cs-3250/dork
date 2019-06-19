# -*- coding: utf-8 -*-
'''basic Dork CLI'''

__all__ = ["main"]

from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.lexers import Lexer

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


class SyntaxLexer(Lexer):
    """NLP Lexer for prompt-toolkit using Spacy
        https://python-prompt-toolkit.readthedocs.io/en/latest/pages/reference.html
        https://github.com/prompt-toolkit/python-prompt-toolkit/
            styles/base.py
            styles/defaults.py
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


def read():
    '''read user CLI input'''
    try:
        return prompt('» ',
                      lexer=SyntaxLexer(),
                      history=FileHistory('history.log'))
    except (EOFError, KeyboardInterrupt):  # ctrl+d & ctrl+c respectively
        return "quit game"


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


def repl():
    '''read–eval–print loop'''
    while True:
        user_input = read()
        stop, output = evaluate(user_input)
        if output:
            print(output)
        if stop:
            exit(0)


def main(*args):  # main CLI runner for Dork
    '''main function'''
    script_name = args[0] if args else '???'
    if "-h" in args or '--help' in args:
        print("usage:", script_name, "[-h]")
    # to do: handle bad arguments
    else:
        repl()
