from exploits.overwrite import Overwrite
from logger import Logger

class CommandHandler:
    exploits = [Overwrite]

    def __init__(self, parser, command):
        for exploit in CommandHandler.exploits:
            if exploit.command == command:
                exploit()
                exit(0)

        Logger.error('Unrecognized command\n')
        parser.print_help()
        exit(1)

