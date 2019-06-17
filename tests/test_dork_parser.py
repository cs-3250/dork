# -*- coding: utf-8 -*-
'''tests for dork parser'''
from dork.parser import Parser


def test_parser_init():
    '''The parser should correctly initialize its parameters.'''
    for input_string in ['', "The quick brown fox jumps over the lazy dog."]:
        parser = Parser(input_string)
        assert hasattr(parser, 'doc')
        assert hasattr(parser, 'chunks')
        assert hasattr(parser, 'command_tokens')
        assert hasattr(parser, 'iteration_index')
