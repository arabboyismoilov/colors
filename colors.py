PUSHTI = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def colored(text, color):
    if color == 'red':
        return f'{FAIL}{text}'
    elif color == 'yellow':
        return f'{WARNING}{text}'
    elif color == 'green':
        return f'{OKGREEN}{text}'
