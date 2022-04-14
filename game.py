import math
import time
from player import HumanPlayer, SmartComputerPlayer


class TicTacToe():          # 
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]  # will use a single list to print 3 x 3 board   

    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
        #  here basically we are saying that which grp of three we are choosing 
        # like first grp 0, 1 , 2 are the row 1 
        # like second grp 3, 4 , 5 are the row 2 
        # like first grp 6, 7 , 8 are the row 3 

    
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 tells the numbers corresponds to each board 
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    
    # function to make a move 
    # here we need two information one is on which squere and ehat is the letter 
    def make_move(self, square, letter):

        if self.board[square] == ' ':
            self.board[square] = letter
        # if it is valid move then we are going to make that block equal to that letter and return true 
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        if all([s == letter for s in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False

    def empty_squares(self):   # it will just return a empty space in board 
        return ' ' in self.board

    def num_empty_squares(self):    # 
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]

    # [ X   X   O ]  --> (0,X) , (1,X), (2, O) 
    # move = []
    # for (i , spot ) in enumerate(self.bvoard) :
    #   if spot == ' ':
    #       move.append(i)
    # returen move  


def play(game, x_player, o_player, print_game=True):            # print_game is true then it will print the board 

    if print_game:
        game.print_board_nums()   

    letter = 'X'          # starting letter 
    # iterate while the game still has empty blocks 
    # we don't have to worry about the winner because we will just return that that will breaks the loop 



    while game.empty_squares():
        # get the move for appropriate player 

        if letter == 'O':      # when the letter is O we are going to ask O_player to move 
            square = o_player.get_move(game)
        else:                  # when the letter is O we are going to ask O_player to move 
            square = x_player.get_move(game)

        # function to make a move 
        # here we need two information one is on which squere and ehat is the letter 
        if game.make_move(square, letter):

            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')          # at the end just print the empty line 

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches playerx means if privious trial is of X then next should be of O


        time.sleep(.8)

    if print_game:
        print('It\'s a tie!')



if __name__ == '__main__':
    x_player = SmartComputerPlayer('X')
    o_player = HumanPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
