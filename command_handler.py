import sys

from exploits.overwrite import Overwrite
from exploits.shellcode import Shellcode

from logger import Logger

class CommandHandler:
    exploits = [Overwrite, Shellcode]

    def __init__(self, parser, command):
        for exploit in CommandHandler.exploits:
            if exploit.command == command:
                exploit()
                sys.exit(0)

        Logger.error('Unrecognized command\n')
        parser.print_help()
        sys.exit(1)

