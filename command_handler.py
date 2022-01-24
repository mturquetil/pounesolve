import sys

from exploits.overwrite import Overwrite
from exploits.shellcode import Shellcode

import logger

def handle(parser, command):
    exploits = [Overwrite, Shellcode]

    for exploit in exploits:
        if exploit.command == command:
            exploit()
            sys.exit(0)

    logger.error('Unrecognized command\n')
    parser.print_help()
    sys.exit(1)
