import numpy as np

from game.games import Game


class Forza4State:
    def __init__(self, board, to_move):
        self.board = board
        self.to_move = to_move


class Forza4(Game):
    def __init__(self, initial_state=None, player='MAX'):
        if initial_state is None:
            board = np.zeros((6, 7))
            initial_state = Forza4State(board=board, to_move=1)
        super(Forza4, self).__init__(initial_state, player)
        self.initial_state = initial_state
        self.player = player

    def actions(self, state: Forza4State):
        """
        Given a state return the list of possible actions
        An action is a tuple (row, col)
        @param state: a state of the game
        @return: a list
        """
        possible_action = [(row, col) for row in range(state.board.shape[0]) for col in range(state.board.shape[1]) if
                           not state.board[row, col] and state.board[row, col - 1]] + [(row, 0) for row in
                                                                                       range(state.board.shape[0]) if
                                                                                       not state.board[row, 0]]
        return possible_action

    def result(self, state: Forza4State, action):
        """
        Given a state and an action returns the reached state
        @param state: a state of the game
        @param action: a possible action in the state
        @return: a new state
        """
        new_board = state.board.copy()
        new_board[action] = state.to_move
        return Forza4State(board=new_board, to_move=self.next_to_move(state))

    def next_to_move(self, state: Forza4State):
        return 1 if state.to_move == - 1 else - 1

    def check_winner(self, state: Forza4State, player):
        row_test = any([any([sum(state.board[i, j:j + 4] * player) == 4 for j in range(4)]) for i in range(state.board.shape[0])])
        col_test = any([any([sum(state.board[j:j + 4, i] * player) == 4 for j in range(3)]) for i in range(state.board.shape[1])])
        return any([row_test, col_test])

    def check_draw(self, state: Forza4State):
        return all([state.board[i, j] != 0 for i in range(state.board.shape[0]) for j in range(state.board.shape[1])])

    def terminal_test(self, state: Forza4State):
        """
        Returns True if the state is a final state (the game is over), False otherwise
        @param state: a state of the game
        @return: True or False
        """

        return self.check_winner(state=state, player=1) or self.check_winner(state=state, player=-1) or self.check_draw(state=state)

    def utility(self, state: Forza4State):
        """
        Given a state returns its utility
        @param state: a state of the game
        @return: a utility value (integer)
        """
        if self.check_winner(state=state, player=1):
            return 1
        if self.check_winner(state=state, player=-1):
            return -1
        if self.check_draw(state=state):
            return 0
        return 0

    def display(self, state: Forza4State):
        print('_____________________')
        print(self.player, 'in \n', state.board)

    def display_move(self, state: Forza4State, move):
        print(self.player, f'--{move}--> \n', state.board)
