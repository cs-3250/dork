# -*- coding: utf-8 -*-
'''basic Dork CLI'''

__all__ = ["main"]


from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.lexers import Lexer

import spacy # natural language processing

from dork import actions

NLP = spacy.load('en_core_web_sm') # language model

ALIASES = {
    #move north > go north
    #go(direct_objects=[['sword'], ['shield'])
    "go":         "move",
    "north":      "go north",
    "n":          "go north",
    #"northeast":  "go northeast",
    #"ne":         "go northeast",
    "east":       "go east",
    "e":          "go east",
    #"southeast":  "go southeast",
    #"se":         "go southeast",
    "south":      "go south",
    "s":          "go south",
    #"southwest":  "go southwest",
    #"sw":         "go southwest",
    "west":       "go west",
    "w":          "go west",
    #"northwest":  "go northwest",
    #"nw":         "go northwest",
    #"give":       "give",
    "q":          "quit"
}


# color scheme: https://github.com/chriskempson/tomorrow-theme
STYLE = {
    'subject':              '#f0c674', # yellow
    'verb':                 '#cc6666', # red
    'adverb':               '#b294bb', # purple
    'direct object':        '#81a2be', # blue
    'indirect object':      '#b5bd68', # green
    'preposition':          '#969896', # gray
    'prepositional object': '#de935f'  # orange
}


# https://python-prompt-toolkit.readthedocs.io/en/latest/pages/reference.html
# https://github.com/prompt-toolkit/python-prompt-toolkit/
    # styles/base.py
    # styles/defaults.py

def chunk_tokens(line):
    '''breaks sentences up into components'''
    chunks = {}
    for token in line:
        if str(token).lower() in ALIASES:
            for subtoken in token.subtree:
                if subtoken is token or subtoken.pos_ == "PART":
                    # particles usually belong to a phrasal verb
                    chunks[subtoken] = "verb"
        elif token.pos_ == "VERB":
            for subtoken in token.subtree:
                if subtoken.pos_ in ["VERB", "PART"]:
                    # particles usually belong to a phrasal verb
                    chunks[subtoken] = "verb"
        elif token.pos_ == "ADV":
            if (token.i > 0) and token.nbor(-1).pos_ == "VERB":
                # a verb followed by an adverb is often a phrasal verb
                chunks[token] = "verb"
            else:
                chunks[token] = "adverb"
        elif token.dep_ == "nsubj":
            # sentence subject - just for testing; not needed for commands
            for subtoken in token.subtree: # contains entire noun phrase
                chunks[subtoken] = "subject"
        elif token.dep_ == "dobj": # direct object
            #TODO break down multiple direct objects joined by conjunctions
            for subtoken in token.subtree:
                chunks[subtoken] = "direct object"
        elif token.dep_ == "dative":
            #TODO break down multiple indirect objects joined by conjunctions
            for subtoken in token.subtree: # contains entire noun phrase
                chunks[subtoken] = "indirect object"
        elif token.dep_ == "pobj":
            if token not in chunks or chunks[token] != "indirect object":
                # if the preposition governing this phrase isn't the dative 'to'
                for subtoken in token.subtree: # contains entire noun phrase
                    chunks[subtoken] = "prepositional object"
            for ancestor in token.ancestors:
                if ancestor.pos_ == "ADP" and ancestor.dep_ == "prep":
                    # preposition governing phrase not likely part of a phrasal verb
                    chunks[ancestor] = "preposition"
        elif token.pos_ == "ADP":
            if (len(line) > token.i + 1) and token.nbor().pos_ == "ADP":
                # if followed by another adposition
                chunks[token] = "verb" # this preposition is likely part of a phrasal verb
            elif token.i > 0:
                if token.nbor(-1).pos_ == "VERB":
                    # if this preposition's leftmost neighbor is a verb...
                        # this preposition is likely part of a phrasal verb
                    chunks[token] = "verb"
                elif token.nbor(-1).pos_ == "ADP":
                    # if this preposition's left neighbor is another adposition...
                        # the left neighbor should've been marked part of a phrasal verb
                    chunks[token] = "preposition"
                elif not token in chunks:
                    chunks[token] = "preposition"
    return chunks


class SyntaxLexer(Lexer):
    '''NLP Lexer for prompt-toolkit using Spacy'''
    def lex_document(self, document):
        def get_line(lineno):
            line = NLP(document.lines[lineno])
            chunks = chunk_tokens(line)
            return [
                (STYLE[chunks[token]] if token in chunks else '',
                 str(token) + token.whitespace_)
                for token in line
                ]
        return get_line


def read():
    '''read user CLI input'''
    try:
        return prompt('» ', lexer=SyntaxLexer(), history=FileHistory('history.log'))
    except (EOFError, KeyboardInterrupt): # ctrl+d & ctrl+c respectively
        print("Goodbye.")
        exit(0)


def evaluate(command):
    '''evaluate user CLI input'''
    user_input = NLP(command)
    chunks = chunk_tokens(user_input)
    verbs = [token for token in chunks if chunks[token] == "verb"]
    while verbs: # decremented below by popping
        verb = '_'.join([str(v) for v in verbs]).lower() # join tokens into string
        if hasattr(actions, verb):
            print("command:  ", verb)
            parameters = {}
            if verbs[-1].i + 1 < len(user_input): # if there is a predicate
                next_neighbor = verbs[-1].nbor()
                predicate = user_input[next_neighbor.i:]
                print("predicate:", predicate)
                adverbs = \
                    [token for token in predicate
                     if token.pos_ in ("ADV", "PART") or token.dep_ == 'advmod']
                if adverbs:
                    parameters['adverbs'] = adverbs
                    print("adverbs:", adverbs)
                direct_objects = \
                    [token for token in chunks
                     if chunks[token] == "direct object"]
                if direct_objects:
                    parameters['direct_objects'] = direct_objects
                    print("direct objects:", direct_objects)
                indirect_objects = \
                    {str(token): [t for t in token.subtree if t is not token]
                     for token in predicate
                     if token.pos_ == "ADP" and token.dep_ == "dative"}
                if indirect_objects:
                    parameters['indirect_objects'] = indirect_objects
                    print("direct objects:", direct_objects)
                    print("indirect objects:", indirect_objects)
                prepositional_phrases = \
                    {str(token): [t for t in token.subtree if t is not token]
                     for token in predicate
                     if token.pos_ == "ADP" and token.dep_ == "prep"}
                if prepositional_phrases:
                    parameters.update(prepositional_phrases)
                    print("prepositional phrases:", prepositional_phrases)
            else: # if there is no predicate
                print("no parameters")
            try:
                return getattr(actions, verb)(**parameters)
            except AttributeError:
                raise NotImplementedError
            break
        elif verb.lower() in ALIASES:
            user_input = NLP(
                ALIASES[verb] + ' ' + \
                 ' '.join([str(token) \
                 for token in user_input \
                 if token not in verbs]))
            chunks = chunk_tokens(user_input)
            verbs = [token for token in chunks if chunks[token] == "verb"]
            continue
        else: # if not hasattr(actions, verb) and not verb.lower() in ALIASES:
            print("guessed:", verb.lower())
            verbs.pop()
    if not verbs:
        print("No command matched.")
        return None

    debugging = False
    if debugging:
        for token in user_input:
            print(token)
            print("pos:", token.pos_)
            print(spacy.explain(token.pos_))
            print("dep:", token.dep_)
            print(spacy.explain(token.dep_))
            print('ancestors: ', [t for t in token.ancestors])
            print('subtree: ', [t for t in token.subtree])
            print()


def repl():
    '''read–eval–print loop'''
    while True:
        command = read()
        output = evaluate(command)
        print(output)

def main(*args): # main CLI runner for Dork
    '''main function'''
    script_name = args[0] if args else '???'
    if "-h" in args or '--help' in args:
        print("usage:", script_name, "[-h]")
    else:
        #print(*args)
        repl()
