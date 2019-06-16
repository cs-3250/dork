# -*- coding: utf-8 -*-
'''lexical chunking'''

import spacy  # natural language processing

from dork import actions
from dork.aliases import ALIASES

NLP = spacy.load('en_core_web_sm')  # language model


class Parser:
    '''dictionary of lexical chunks'''

    # TODO detect multiple verbs
    #   split multiple objects coordinated by conjunctions:
    #     e.g. attack the mummy and the ghoul

    # TODO detect multiple verbs
    #   decide whether it's they are coordinated by a conjunction:
    #     e.g. help go; try to dance
    #   or one is subordinate:
    #     e.g. wine and dine

    def __init__(self, text):
        self.debugging = True
        self.initialize(text)
        self.command_tokens = []
        self.iteration_index = 0

    def initialize(self, text):
        ''' called by __init__,
            but also used by resolve_alias() to reinitialize'''
        self.doc = NLP(text)
        # if self.debugging:
        #     self.print_token_info()
        self.chunks = {}
        for token in self.doc:
            if str(token).lower() in ALIASES:
                self.chunk_alias(token)
            elif token.pos_ == "VERB":
                self.chunk_verb(token)
            elif token.pos_ == "ADV":
                self.chunk_adverb(token)
            elif token.dep_ == "nsubj":
                self.chunk_subject(token)
            elif token.dep_ == "dobj":  # direct object
                self.chunk_direct_object(token)
            elif token.dep_ == "dative":
                self.chunk_indirect_object(token)
            elif token.dep_ == "pobj":
                self.chunk_prepositional_object(token)
            elif token.pos_ == "ADP":
                self.chunk_adposition(token)

    def print_token_info(self):
        '''print out Spacy metadata for each token'''
        for token in self.doc:
            print(token)
            print("pos:", token.pos_)
            print(spacy.explain(token.pos_))
            print("dep:", token.dep_)
            print(spacy.explain(token.dep_))
            print('ancestors: ', [t for t in token.ancestors])
            print('subtree: ', [t for t in token.subtree])
            print()

    def __len__(self):
        return len(self.doc)

    def __iter__(self):
        self.iteration_index = 0
        return self

    def __next__(self):
        '''returns the next token for iteration'''
        if self.iteration_index < len(self.doc):
            result = self.doc[self.iteration_index]
            self.iteration_index += 1
            return result
        raise StopIteration

    def __getitem__(self, index):
        return self.doc[index]

    def __str__(self):
        return str(self.doc)

    def chunk_alias(self, token):
        '''chunk a token with a matching entry in ALIASES'''
        for subtoken in token.subtree:
            if subtoken is token or subtoken.pos_ == "PART":
                # particles usually belong to a phrasal verb
                self.chunks[subtoken] = "verb"

    def chunk_verb(self, token):
        '''chunk a verb token'''
        for subtoken in token.subtree:
            if subtoken.pos_ in ["VERB", "PART"]:
                # particles usually belong to a phrasal verb
                self.chunks[subtoken] = "verb"

    def chunk_adverb(self, token):
        '''chunk an adverb token'''
        if (token.i > 0) and token.nbor(-1).pos_ == "VERB":
            # a verb followed by an adverb is often a phrasal verb
            self.chunks[token] = "verb"
        else:
            self.chunks[token] = "adverb"

    def chunk_subject(self, token):
        '''chunk a subject token'''
        # just for testing; should not be needed for commands,
        # since English imperatives contain no explicit subject
        for subtoken in token.subtree:  # contains entire noun phrase
            self.chunks[subtoken] = "subject"

    def chunk_direct_object(self, token):
        '''chunk a direct object token'''
        # TODO break down multiple direct objects joined by conjunctions
        for subtoken in token.subtree:
            self.chunks[subtoken] = "direct object"

    def chunk_indirect_object(self, token):
        '''chunk an indirect object token'''
        # TODO break down multiple indirect objects joined by conjunctions
        for subtoken in token.subtree:  # contains entire noun phrase
            self.chunks[subtoken] = "indirect object"

    def chunk_prepositional_object(self, token):
        '''chunk a prepositional object token'''
        if token not in self.chunks or self.chunks[token] != "indirect object":
            # if the preposition governing this phrase isn't the dative 'to'
            for subtoken in token.subtree:  # contains entire noun phrase
                self.chunks[subtoken] = "prepositional object"
        for ancestor in token.ancestors:
            if ancestor.pos_ == "ADP" and ancestor.dep_ == "prep":
                # governing preposition not likely part of a phrasal verb
                self.chunks[ancestor] = "preposition"

    def chunk_adposition(self, token):
        '''chunk an adposition token'''
        if (len(self.doc) > token.i + 1) and token.nbor().pos_ == "ADP":
            # if followed by another adposition...
            # this preposition is likely part of a phrasal verb
            self.chunks[token] = "verb"
        elif token.i > 0:
            if token.nbor(-1).pos_ == "VERB":
                # if this preposition's leftmost neighbor is a verb...
                #   this preposition is likely part of a phrasal verb
                self.chunks[token] = "verb"
            elif token.nbor(-1).pos_ == "ADP":
                # if this preposition's left neighbor is another adposition...
                #   the left neighbor was marked part of a phrasal verb
                self.chunks[token] = "preposition"
            elif token not in self.chunks:
                self.chunks[token] = "preposition"

    @property
    def verbs(self):
        """ initial guess at which tokens could comprise an action
            returns: those tokens
        """
        return [token for token in self.doc
                if token in self.chunks
                and self.chunks[token] == "verb"]

    def resolve_alias(self, alias, alias_tokens):
        """ substitute alias in user input with actual command name, reparse
            returns: new verb tokens after reparsing
        """
        self.initialize(ALIASES[alias.lower()] + ' ' +
                        ' '.join([str(token)
                                  for token in self.doc
                                  if token not in alias_tokens]))
        return self.verbs

    def resolve_action(self):
        """ determine whether user input can be resolved to an action function
            returns: the name of the action function or None
        """
        self.command_tokens = self.verbs
        while self.command_tokens:  # decremented below by popping
            command = '_'.join(  # join tokens into a string
                [str(v) for v in self.command_tokens]).lower()
            if hasattr(actions, command):
                print("command:  ", command)
                return command
            if command.lower() in ALIASES:
                self.command_tokens = \
                    self.resolve_alias(command, self.command_tokens)
                continue
            else:  # if command in neither actions nor ALIASES:
                if self.debugging:
                    print("guessed:  ", command.lower())
                self.command_tokens.pop()
        if not self.command_tokens:
            print("No command matched.")
            return None

    @property
    def parameters(self):
        '''dictionary of parameters for action function'''
        parameters = {}

        # if there is a predicate:
        if self.command_tokens[-1].i + 1 < len(self):
            next_neighbor = self.command_tokens[-1].nbor()
            predicate = self.doc[next_neighbor.i:]
            print("predicate:", predicate)

            adverbs = \
                [token for token in predicate
                 if token.pos_ in ("ADV", "PART") or token.dep_ == 'advmod']
            if adverbs:
                parameters['adverbs'] = Arguments(adverbs)

            direct_objects = \
                [token for token in self.doc
                 if token in self.chunks
                 and self.chunks[token] == "direct object"]
            if direct_objects:
                parameters['direct_objects'] = Arguments(direct_objects)

            indirect_objects = \
                {str(token): [t for t in token.subtree if t is not token]
                 for token in predicate
                 if token.pos_ == "ADP" and token.dep_ == "dative"}
            if indirect_objects:
                parameters['indirect_objects'] = Arguments(indirect_objects)

            prepositional_phrases = \
                {str(token):
                 Arguments([t for t in token.subtree if t is not token])
                 for token in predicate
                 if token.pos_ == "ADP" and token.dep_ == "prep"}
            if prepositional_phrases:
                parameters.update(prepositional_phrases)

            if self.debugging:
                for parameter in parameters:
                    print(parameter + ':', parameters[parameter])

        else:  # if there is no predicate
            print("no parameters")

        return parameters


class Arguments:
    """ a list of arguments, each of which consists of a lists of tokens
        can be treated as a single string
    """

    # TODO: create Argument object...
    #   to also facilitate string representation of individual list elements

    def __init__(self, *args):
        self.arguments = [argument for argument in args]

    def __str__(self):
        return ' '.join([
            ' '.join([token.text for token in argument])
            for argument in self.arguments])

    def __add__(self, other):
        return str(self) + other

    def __radd__(self, other):
        return other + str(self)
