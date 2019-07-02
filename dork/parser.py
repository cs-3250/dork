# -*- coding: utf-8 -*-
'''lexical chunking'''

import builtins

import spacy  # natural language processing
from spacy.symbols import ADP, ADV, PART, VERB, \
    advmod, dobj, nsubj, pobj, prep

from dork import actions
from dork.aliases import ALIASES

NLP = spacy.load('en_core_web_sm')  # language model

ACTION_LIST = [action.rstrip('_') for action in actions.__dict__
               if callable(getattr(actions, action))]


class Parser:
    '''dictionary of lexical chunks'''

    # to do: detect multiple verbs
    #   split multiple objects coordinated by conjunctions:
    #     e.g. attack the mummy and the ghoul

    # to do: detect multiple verbs
    #   decide whether it's they are coordinated by a conjunction:
    #     e.g. help go; try to dance
    #   or one is subordinate:
    #     e.g. wine and dine

    # to do: also pass the original user input which mapped to a command
    #   e.g. so if the user types "exit house", but 'exit' maps to quit()...
    #     a function will be able to respond appropriately, like:
    #       "I don't know what you want to exit."
    #     instead of:
    #       "I don't know what you want to quit."

    def __init__(self, text):
        self.debugging = False  # to do: add a command to enable debugging
        self.doc = NLP(text)
        self.chunks = Parser.chunk(self.doc)
        self.command_tokens = []
        self.iteration_index = 0

    @staticmethod
    def chunk(doc):
        """ called by __init__ and resolve_alias()
            returns: (parsed Spacy Doc, dict of chunk assignments)"""
        chunks = {}
        for token in doc:
            if token.lower_ in ACTION_LIST or token.lower_ in ALIASES:
                chunks.update(Parser.chunk_action(token))
            elif token.pos == VERB:
                chunks.update(Parser.chunk_verb(token))
            elif token.pos == ADV:
                chunks.update(Parser.chunk_adverb(token))
            elif token.dep == nsubj:
                chunks.update(Parser.chunk_subject(token))
            elif token.dep == dobj:  # direct object
                chunks.update(Parser.chunk_direct_object(token))
            elif token.dep_ == 'dative':
                chunks.update(Parser.chunk_indirect_object(token))
            elif token.dep == pobj:
                chunks.update(Parser.chunk_prepositional_object(token, chunks))
            elif token.pos == ADP:
                chunks.update(Parser.chunk_adposition(token, chunks))
        return chunks

    @staticmethod
    def print_token_info(doc):
        '''print out Spacy metadata for each token'''
        for token in doc:
            print("token:", token)
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

    @staticmethod
    def chunk_action(token):
        '''chunk a token with a matching entry in ALIASES'''
        chunks = {}
        for subtoken in token.subtree:
            if subtoken is token or subtoken.pos == PART:
                # particles usually belong to a phrasal verb
                chunks[subtoken] = "verb"
        return chunks

    @staticmethod
    def chunk_verb(token):
        '''chunk a verb token'''
        chunks = {}
        for subtoken in token.subtree:
            if subtoken.pos in [VERB, PART]:
                # particles usually belong to a phrasal verb
                chunks[subtoken] = "verb"
        return chunks

    @staticmethod
    def chunk_adverb(token):
        '''chunk an adverb token'''
        chunks = {}
        if (token.i > 0) and token.nbor(-1).pos == VERB:
            # a verb followed by an adverb is often a phrasal verb
            chunks[token] = "verb"
        else:
            chunks[token] = "adverb"
        return chunks

    @staticmethod
    def chunk_subject(token):
        '''chunk a subject token'''
        # just for testing; should not be needed for commands,
        # since English imperatives contain no explicit subject
        chunks = {}
        for subtoken in token.subtree:  # contains entire noun phrase
            chunks[subtoken] = "subject"
        return chunks

    @staticmethod
    def chunk_direct_object(token):
        '''chunk a direct object token'''
        # to do: break down multiple direct objects joined by conjunctions
        chunks = {}
        for subtoken in token.subtree:
            chunks[subtoken] = "direct object"
        return chunks

    @staticmethod
    def chunk_indirect_object(token):
        '''chunk an indirect object token'''
        # to do:: break down multiple indirect objects joined by conjunctions
        chunks = {}
        for subtoken in token.subtree:  # contains entire noun phrase
            chunks[subtoken] = "indirect object"
        return chunks

    @staticmethod
    def chunk_prepositional_object(token, chunks):
        '''chunk a prepositional object token'''
        if token not in chunks or chunks[token] != "indirect object":
            # if the preposition governing this phrase isn't the dative 'to'
            for subtoken in token.subtree:  # contains entire noun phrase
                chunks[subtoken] = "prepositional object"
        for ancestor in token.ancestors:
            if ancestor.pos == ADP and ancestor.dep == prep:
                # governing preposition not likely part of a phrasal verb
                chunks[ancestor] = "preposition"
        return chunks

    @staticmethod
    def chunk_adposition(token, chunks):
        '''chunk an adposition token'''
        chunks = {}
        if (len(token.doc) > token.i + 1) and token.nbor().pos == ADP:
            # if followed by another adposition...
            # this preposition is likely part of a phrasal verb
            chunks[token] = "verb"
        elif token.i > 0:
            if token.nbor(-1).pos == VERB:
                # if this preposition's leftmost neighbor is a verb...
                #   this preposition is likely part of a phrasal verb
                chunks[token] = "verb"
            elif token.nbor(-1).pos == ADP:
                # if this preposition's left neighbor is another adposition...
                #   the left neighbor was marked part of a phrasal verb
                chunks[token] = "preposition"
            elif token not in chunks:
                chunks[token] = "preposition"
        return chunks

    @property
    def verbs(self):
        """ initial guess at which tokens could comprise an action
            returns: those tokens
        """
        return [token for token in self.doc
                if token in self.chunks
                and (self.chunks[token] == "verb"
                     or token.lower_ in ACTION_LIST)]

    def resolve_alias(self, alias, alias_tokens):
        """ substitute alias in user input with actual command name, reparse
            returns: new verb tokens after reparsing
        """
        # to do: save resolved doc & chunk distinct from original
        resolved_text = ALIASES[alias.lower()] + ' ' + \
            ' '.join([str(token)
                      for token in self.doc
                      if token not in alias_tokens])
        self.doc = NLP(resolved_text)
        self.chunks = Parser.chunk(self.doc)
        return self.verbs

    def resolve_action(self):
        """ determine whether user input can be resolved to an action function
            returns: the name of the action function or None
        """
        self.command_tokens = self.verbs
        while self.command_tokens:  # decremented below by popping
            command = '_'.join(  # join tokens into a string
                [v.lower_ for v in self.command_tokens])
            if command in dir(builtins):
                command = command + '_'
            if hasattr(actions, command):
                if self.debugging:
                    print("matched:  ", command.lower())
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
            parameters['predicate'] = Arguments(predicate)

            # to do: work on making this a list of spans
            verbs = \
                [token for token in predicate
                 if token.pos == VERB]
            if verbs:
                parameters['verbs'] = Arguments(*verbs)

            adverbs = \
                [token for token in predicate
                 if token.pos in (ADV, PART) or token.dep == advmod]
            if adverbs:
                parameters['adverbs'] = Arguments(*adverbs)

            direct_objects = \
                [chunk for chunk in self.doc.noun_chunks
                 if chunk.root.dep == dobj]
            if direct_objects:
                parameters['direct_objects'] = Arguments(*direct_objects)

            indirect_objects = \
                [chunk for chunk in self.doc.noun_chunks
                 if chunk.root.dep_ == 'dative']
            if indirect_objects:
                parameters['indirect_objects'] = Arguments(*indirect_objects)

            prepositional_phrases = \
                {str(token):
                 Arguments([t for t in token.subtree if t is not token])
                 for token in predicate
                 if token.pos == ADP and (token.dep == prep
                                          or token.dep_ == 'dative')}
            if prepositional_phrases:
                parameters.update(prepositional_phrases)

            if self.debugging:
                for parameter in parameters:
                    print('{:15} {}'.format(parameter + ':',
                                            str(parameters[parameter])))

        else:  # if there is no predicate
            if self.debugging:
                print("no parameters")

        return parameters


class Arguments:
    """ internally, a list of Argument objects; may be treated as a single string
        constructor takes an arbitrary number of spacy spans or tokens
        Argument objects are accessible by index, i.e. Arguments[index].
        len(Arguments) returns the number of Argument objects contained.
    """

    # to do: create Argument object...
    #   to also facilitate string representation of individual list elements

    def __init__(self, *args):
        self.arguments = [Argument(arg) for arg in args]

    def __len__(self):
        return len(self.arguments)

    def __getitem__(self, index):
        return self.arguments[index]

    def __str__(self):
        return ' '.join([str(argument) for argument in self.arguments])

    def __eq__(self, other):
        if self is other:
            return True
        if str(self) == other:
            return True
        return False

    def __add__(self, other):
        return str(self) + other

    def __radd__(self, other):
        return other + str(self)

    def strip(self, characters):
        '''wrapper around str(self).strip()'''
        return str(self).strip(characters)


# to do: the right way to do this
class Argument:
    """ wrapper around a spacy Token or Span object
        inner spacy object is accessible via Argument.contents
        may be treated as a string"""

    def __init__(self, argument):
        if isinstance(argument, (spacy.tokens.Token, spacy.tokens.Span)):
            self.contents = argument
        else:
            raise TypeError("Expected spacy Span or list of Tokens; "
                            + "got argument of type "
                            + type(argument).__name__ + ": "
                            + str(argument) + '.')

    def __len__(self):
        return len(str(self))

    def __str__(self):
        return self.contents.text

    def __eq__(self, other):
        if self is other:
            return True
        if str(self) == other:
            return True
        return False

    def __add__(self, other):
        return str(self) + other

    def __radd__(self, other):
        return other + str(self)

    def strip(self, characters):
        '''wrapper around str(self).strip()'''
        return str(self).strip(characters)
