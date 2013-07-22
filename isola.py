import sys
import subprocess


class Board():

    SQUARE = '-'
    EMPTY = ' '

    def __init__(self):
        self.board = [['-']*7 for i in range(7)]
        self.p1 = {'x': 3, 'y': 0}
        self.p2 = {'x': 3, 'y': 6}
        self.board[self.p1['y']][self.p1['x']] = 'O'
        self.board[self.p2['y']][self.p2['x']] = 'X'

    def __str__(self):
        return '\n'.join([' '.join(line) for line in self.board])

    def get_board_with_move_applied_if_move_is_legal(self, player, move):
        new_board = [line[:] for line in self.board]
        move = move.split(',')
        if len(move) != 4:
            return False
        try:
            dx = int(move[0])
            dy = int(move[1])
        except:
            return False
        if abs(dx) > 1 or abs(dy) > 1:
            return False

        if self.board[player['y'] + dy][player['x'] + dx] != Board.SQUARE:
            return False

        new_board[player['y'] + dy][player['x'] + dx] = \
            new_board[player['y']][player['x']]
        new_board[player['y']][player['x']] = Board.SQUARE

        try:
            remove_x = int(move[2])
            remove_y = int(move[3])
        except:
            return False

        if new_board[remove_y][remove_x] != Board.SQUARE:
            return False

        new_board[remove_y][remove_x] = Board.EMPTY
        player['y'] += dy
        player['y'] += dx

        return new_board

    def try_move(self, player, move):
        new_board = self.get_board_with_move_applied_if_move_is_legal(
            player, move)
        if new_board is not False:
            self.board = new_board
        else:
            raise Exception("Illegal move!")

    def get_player_repr(self, player):
        return self.board[player['y']][player['x']]

    def get_board_state(self):
        return ''.join([''.join(line) for line in self.board])


def main():

    board = Board()

    board.p1['runnable'] = sys.argv[1]
    board.p2['runnable'] = sys.argv[2]

    player = board.p1

    def swap_players():
        return board.p2 if player == board.p1 else board.p1

    while True:
        print board
        print ''
        move = subprocess.Popen(' '.join([
            player['runnable'],
            board.get_player_repr(player),
            '"' + board.get_board_state() + '"'
        ]), shell=True, stdout=subprocess.PIPE).communicate()[0]
        try:
            board.try_move(player, move)
            player = swap_players()
        except Exception, e:
            print e
            break

    player = swap_players()
    print 'winner is: ' + board.get_player_repr(player)

main()
