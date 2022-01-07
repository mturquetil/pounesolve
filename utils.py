from logger import Logger
import os

def check_binary(binary):
    print()
    print(f'{Logger.custom("CHECKING FILE", style="bold")}: {Logger.custom(binary, color="blue", style="bold")}')

    if binary.is_file():
        Logger.success('Path provided is a file')
    else:
        Logger.error('Path provided is not a file or does not exist')
        exit(1)

    if os.access(binary, os.R_OK | os.X_OK):
        Logger.success('Correct permissions')
    else:
        Logger.error('Read and execute permissions are needed')
        exit(1)

    print()

    return True
