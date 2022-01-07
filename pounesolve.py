#!/usr/bin/env python

import argparse, sys, inspect
from logger import Logger
from command_handler import CommandHandler

class PouneSolve:
    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Automation tool for binary exploitation',
            usage='''pounesolve <command> [<args>]

Available commands:
  overwrite     Try instruction pointer overwrite to access specific part of the binary
  shellcode     Try to insert executable code in the binary and execute it

''')
        parser.add_argument('command', nargs='?', help='Subcommand to run')
        args = parser.parse_args(sys.argv[1:2])

        if not args.command:
            parser.print_help()
            exit(1)

        CommandHandler(parser, args.command)

if __name__ == '__main__':
    PouneSolve()
