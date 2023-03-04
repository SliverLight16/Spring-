import time
from unbeattac import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer

class TicTacToe:
    def __init__(self):
            self.board = [' ' for _ in range(9)] #using a single list to rep the 3x3 board
            self.current_winner = None #keep track of 

    def print_board(self):
        #organizing the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2  will rep the first row of three boxes and so on
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
       return [i for i, spot in enumerate(self.board) if spot == ' ']
        # i guess each space in the board is auto assigned a space
        # but if the space is filled will x or o then you cant move there
        # therefore you cant move there
    
    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return len(self.available_moves())
        # return self.board.count(' ')

    def make_move(self, square, letter):
        #if valid move, then make the move (assign a square to a letter)
        #then return True, if invalid, then return False 
        print("Sqaure: ", self.board) #Debugging Line
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # we have to check all poss. for a win

        #check rows
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) *3]
        if all([spot == letter for spot in row]):
            return True

        #check columns
        col_ind = square % 3 
        column = [self.board[col_ind+i*3]for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        #check diagnol
        #but only if the square is an even number (0, 2, 4, 6, 8)
        #these are the only poss. squares to use to win w/ a diagnol
        if square % 2 == 0:
            diagnol1 = [self.board[i] for i in [0, 4, 8]] # left to right
            if all([spot == letter for spot in diagnol1]):
                return True

            diagnol2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagnol2]):
                return True 

        # if all checks fail, no one won, yet
        return False
        

def play(game, x_player, o_player, print_game=True):
    # return the winner and letter, or None for tie
    if print_game:
        game.print_board_nums()

    letter = 'X' # starting letter
    #iterate while the game still has empty squares 
    # it'll return the winner and break the loop

    while game.empty_squares():
        if letter == 'O': # get the move form approiate player
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game) 

        # function defined above to dictate how moves will operate
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('') #just an empty live

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter


            # obvi need to alternarte playerasd
            letter = 'O' if letter == 'X' else 'X'
        
        # a pause between the user's move and computer's
        time.sleep(0.8)

    if print_game:
        print('It\'s a tie')


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = GeniusComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)