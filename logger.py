INFO = '\033[94m'
SUCCESS = '\033[92m\033[1m'
WARNING = '\033[93m\033[1m'
ERROR = '\033[91m\033[1m'

# styles
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

# colors
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'

END = '\033[0m'


def info(content):
    print(f'[{INFO}i{END}] {content}')

def success(content):
    print(f'[{SUCCESS}+{END}] {content}')

def warning(content):
    print(f'[{WARNING}!{END}] {content}')

def error(content):
    print(f'[{ERROR}x{END}] {content}')

def custom(content, color = None, style = None):
    wrapper = ''

    if color:
        wrapper += globals()[color.upper()]

    if style:
        wrapper += globals()[style.upper()]

    return f'{wrapper}{content}{END}'
