# -*- coding: utf-8 -*-
'''tests for dork parser'''

import spacy
from spacy.symbols import PUNCT
from dork.parser import Parser

NLP = spacy.load('en_core_web_sm')


def test_parser_init():
    '''The parser should correctly initialize its parameters.'''
    for input_string in ['', "The quick brown fox jumped over the lazy dog."]:
        parser = Parser(input_string)
        assert hasattr(parser, 'doc')
        assert hasattr(parser, 'chunks')
        assert hasattr(parser, 'command_tokens')
        assert hasattr(parser, 'iteration_index')


def test_chunker():
    """ The chunker should output a dictionary entry for each token in
        the document, in order to assign it to a chunk."""
    for input_string in ['', "The brown fox quickly picked "
                         + "the angry dog a flower for Festivus."]:
        parser = Parser(input_string)
        assert isinstance(parser.chunks, dict)
        assert len(parser.chunks) == len([token for token in parser.doc
                                          if token.pos != PUNCT])


def test_debug_output(capsys):
    """ dork.parser.print_token_info() should print debugging information
        for the tokens in a document."""
    doc = NLP("The quick brown fox jumped over the lazy dog.")
    Parser.print_token_info(doc)
    assert capsys.readouterr()
