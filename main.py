from parse_line import *
from call_other import *
def main():
    line = ''
    
    print('Welcome to Ban-Terminal!\nType "help" for help.')
    while True:
        line = input('> ')
        line_result = parse_line(line)
        call_other(line_result[0], line_result[1])
if __name__ == '__main__':
    main()