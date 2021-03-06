import os
import sys

import logger


def check_binary(binary):
    print(f'\n{logger.custom("CHECKING FILE", style="bold")}: {logger.custom(binary.path, color="blue", style="bold")}')

    if binary.posix_path.is_file():
        logger.success("Path provided is a file\n")
    else:
        logger.error("Path provided is not a file or does not exist\n")
        sys.exit(1)

    if os.access(binary.path, os.R_OK | os.X_OK):
        logger.success("Correct permissions\n")
    else:
        logger.error("Read and execute permissions are needed\n")
        sys.exit(1)

    return True
