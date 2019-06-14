# -*- coding: utf-8 -*-
# basic Dork CLI

__all__ = ["main"]


def main(*args): # main CLI runner for Dork

    script_name = args[0] if args else '???'
    if "-h" in args or '--help' in args:
        print("usage:", script_name, "[-h]")
    else:
        print(*args)
