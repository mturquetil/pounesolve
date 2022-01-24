#!/usr/bin/env python

import argparse
import sys

import command_handler
import pwn

pwn.context.log_level = 'error'

def main():
    parser = argparse.ArgumentParser(
        description='Automation tool for binary exploitation',
        usage='''main.py <command>

Available commands:
overwrite     Try instruction pointer overwrite to access specific part of the binary
shellcode     Try to insert executable code in the binary and execute it

''')
    parser.add_argument('command', nargs='?', help='Subcommand to run')
    args = parser.parse_args(sys.argv[1:2])

    if not args.command:
        parser.print_help()
        sys.exit(1)

    command_handler.handle(parser, args.command)


if __name__ == '__main__':
    main()
