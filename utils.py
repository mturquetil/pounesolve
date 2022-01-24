from logger import Logger

import os
import sys

def check_binary(binary):
    print(f'\n{Logger.custom("CHECKING FILE", style="bold")}: {Logger.custom(binary.path, color="blue", style="bold")}')

    if binary.posix_path.is_file():
        Logger.success('Path provided is a file\n')
    else:
        Logger.error('Path provided is not a file or does not exist\n')
        sys.exit(1)

    if os.access(binary.path, os.R_OK | os.X_OK):
        Logger.success('Correct permissions\n')
    else:
        Logger.error('Read and execute permissions are needed\n')
        sys.exit(1)

    return True
