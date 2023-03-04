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
        square = random.choice(game.available_moves())
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
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True

            except ValueError:
                print('Invalid square. Try Again.')

        return val
    
class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves()) # randomly choose square at beginning of game

        else: #Implementing the algorithm that will be able to determine the best possible moves for in order to win
            square = self.minimax(game, self.letter)['position']
        return square
    
    def minimax(self, state, player):
        max_player = self.letter #yourself
        other_player = 'O' if player == 'X' else 'X' # bascially use the letter not taken

        # first we need to check if the previous move was a winning one
        # this is called a base case
        if state.current_winner == other_player:
            # we need to return the position and score b/c we need to track of score for minimax to work
            return {'position': None,
                    'score': 1 * (state.num_empty_squares() +1 ) if other_player == max_player else -1 * (
                    state.num_empty_squares() +1)
                    }
        
        elif not state.empty_squares(): # no empty squares
            return {'position': None, 'score': 0}
        
        if player == max_player:
            best = {'position': None, 'score': -math.inf} # each score should maximize 

        else:
            best = {'position': None, 'score': math.inf} # each score should minimize

        for possible_move in state.available_moves():
            # step 1 make a move
            state.make_move(possible_move, player)
            # step 2 recurse using minimax to slimulate a game after making that move
            sim_score = self.minimax(state, other_player)
            # step 3 undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move
            # step 4: update the dictionaries (the curly brackets) if ness
            if player == max_player: # maximize the max_player chances of winning
                if sim_score['score'] > best['score']:
                    best = sim_score
            
            else: # but minimize the other players chances of losing
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best



