import random

from game.games import Game


class TTTState:
    def __init__(self, board, to_move):
        self.board = board
        self.to_move = to_move


class TicTacToe(Game):
    def __init__(self, initial_state=None, player='MAX'):
        if initial_state is None:
            board = [[None] * 3] * 3
            initial_state = TTTState(board=board, to_move=1)
        super(TicTacToe, self).__init__(initial_state, player)
        self.initial_state = initial_state
        self.player = player

    def actions(self, state: TTTState):
        """
        Given a state return the list of possible actions
        An action is the position where the player specified in the attribute to_move of TTTState
        will put its signature (1 or -1)
        The position will be a tuple (row, column)
        @param state: a state of the game
        @return: a list
        """
        possible_actions = [(row, col) for row in range(len(state.board)) for col in range(len(state.board[row])) if
                            not state.board[row][col]]
        random.shuffle(possible_actions)
        return possible_actions

    def result(self, state: TTTState, action):
        """
        Given a state and an action returns the reached state
        @param state: a state of the game
        @param action: a possible action in the state
        @return: a new state
        """
        new_board = [list(state.board[i]) for i in range(len(state.board))]
        new_board[action[0]][action[1]] = state.to_move
        return TTTState(board=new_board, to_move=self.next_to_move(state))

    def next_to_move(self, state: TTTState):
        """
        given a state returns the next player to move
        @param state: TTTState
        @return: 1 or -1
        """
        return -1 if state.to_move == 1 else 1

    def check_winner(self, state: TTTState, player):
        """
        Given a state and a player returns  True if that player has won
        @param state: TTTState
        @return: True or False
        """
        row = any(
            [all([state.board[i][j] == player for j in range(len(state.board[i]))]) for i in range(len(state.board))])
        col = any(
            [all([state.board[j][i] == player for j in range(len(state.board[i]))]) for i in range(len(state.board))])
        diag = any([all([state.board[i][i] == player for i in range(len(state.board))]),
                    all([state.board[i][len(state.board) - 1 - i] == player for i in range(len(state.board))])])
        return any([row, col, diag])

    def check_draw(self, state: TTTState):
        return sum([1 for row in range(len(state.board)) for col in range(len(state.board[row])) if
                    not state.board[row][col]]) == 0

    def terminal_test(self, state: TTTState):
        """
        Returns True if the state is a final state (the game is over), False otherwise
        @param state: a state of the game
        @return: True or False
        """
        result_x = self.check_winner(state=state, player=1)
        result_y = self.check_winner(state=state, player=-1)
        draw = self.check_draw(state)
        return any([result_x, result_y, draw])

    def utility(self, state: TTTState):
        """
        Given a state returns its utility
        @param state: a state of the game
        @return: a utility value (integer)
        """
        if self.check_winner(state, 1):
            return 1
        if self.check_winner(state, -1):
            return -1
        if self.check_draw(state):
            return 0

    @staticmethod
    def print_chess(state: TTTState):
        print('\t', end='')
        print('\n___________________')

        for row in range(len(state.board)):
            print('|', end='')
            for col in range(len(state.board)):
                if state.board[row][col] == 1:
                    print('  X  ', end='')
                elif state.board[row][col] == -1:
                    print('  O  ', end='')
                else:
                    print('     ', end='')
                print('|', end='')
            print('\n', end='')
            print('___________________')

    def display(self, state: TTTState):
        print('_____________________')
        print(self.player, 'in ', state.board)
        self.print_chess(state)

    def display_move(self, state: TTTState, move):
        print(self.player, f'--{move}--> ', state.board)
        self.print_chess(state)
