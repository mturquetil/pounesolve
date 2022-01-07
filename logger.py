class Logger:
    # types
    INFO = '\033[94m'
    SUCCESS = '\033[92m\033[1m'
    WARNING = '\033[93m\033[1m'
    ERROR = '\033[91m\033[1m'

    # styles
    ITALIC = '\033[3;31m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BACKGROUND = '\033[7;31m'

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
        print(f'[{Logger.INFO}i{Logger.END}] {content}')

    def success(content):
        print(f'[{Logger.SUCCESS}+{Logger.END}] {content}')

    def warning(content):
        print(f'[{Logger.WARNING}!{Logger.END}] {content}')

    def error(content):
        print(f'[{Logger.ERROR}x{Logger.END}] {content}')

    def custom(content, color = None, style = None):
        wrapper = ''

        if color:
            wrapper += getattr(Logger, color.upper())

        if style:
            wrapper += getattr(Logger, style.upper())

        return f'{wrapper}{content}{Logger.END}'


