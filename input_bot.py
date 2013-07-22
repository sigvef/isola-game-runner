import sys


def main():
    player = sys.argv[1]
    board = sys.argv[2]
    sys.stderr.write('[INPUT BOT] I was told I was player ' + player + '\n')
    sys.stderr.write(
        '[INPUT BOT] I was told that the board looks like this: ' +
        board + '\n')
    sys.stderr.write('[INPUT BOT] What move should I do?')
    sys.stderr.write(' (format: dx,dy,remove_x,remove_y): ')
    print raw_input()

main()
