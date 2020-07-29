"""

Desc:               Tic-Tac-Toe
CreatedOn:          2020/7/23 17:31
Author:             wut
"""

from collections import Counter


class TicTacToe:
    def __init__(self):
        self._board = TicTacToe.init_board()

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, value_pos):
        value, pos = value_pos
        x, y = pos
        if not self._board[x][y]:
            self._board[x][y] = value
        else:
            raise

    @staticmethod
    def init_board():
        return [[0] * 3 for _ in range(3)]

    def reset(self):
        self._board = TicTacToe.init_board()

    @staticmethod
    def win_or_not(*pos):
        if len(pos) < 3:
            return False

        xy_equal = len([item for item in pos if item[0] == item[1]])
        x, y = zip(*pos)
        x_equal = max(Counter(x).values())
        y_equal = max(Counter(y).values())
        return True if any([xy_equal >= 3, x_equal >= 3, y_equal >= 3, sum(x) == sum(y)]) else False

    def find_user(self, value):
        rs = []
        for x, item_x in enumerate(self.board):
            for y, item_y in enumerate(item_x):
                if item_y == value:
                    rs.append((x, y))
        return rs

    def show(self):
        for item in self.board:
            print(item)


def main():
    ttt = TicTacToe()
    start_signal = input('Want To Play TicTacToe? (Y/N)')
    if start_signal.upper() == 'Y':
        while True:
            i = 0
            while i < 3 * 3:
                value = (i % 2) + 1
                pos = eval(input('Player{value} input position:'.format(value=value)))
                try:
                    ttt.board = (value, pos)
                except:
                    print('this position exist value, please put again...')
                    i -= 1
                ttt.show()
                rs = ttt.find_user(value)
                is_win = TicTacToe.win_or_not(*rs)
                if is_win:
                    print('Player{value} win!'.format(value=value))
                    ttt.reset()
                    break
                i += 1
            end_signal = input('Want To Quit? (Y/N)')
            if end_signal.upper() == 'Y':
                break


if __name__ == "__main__":
    main()
