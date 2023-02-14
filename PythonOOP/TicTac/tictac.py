import math
import random

class Player:
    def __init__(self, letter):
        #letter is X or O
        self.letter = letter
    
    #we want the players to get their move
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.avaliable_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            
            #we are making sure: 
            # 1 that the user inputted integer is 0-9 (valid)
            # 2 that the square is not taken

            try: 
                val = int(square)
                if val not in game.avaliable_moves():
                    raise ValueError
                valid_square = True

            except ValueError:
                print('Invalid square. Try Again.')

        return val