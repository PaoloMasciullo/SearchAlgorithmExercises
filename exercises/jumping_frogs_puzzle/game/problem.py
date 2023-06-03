from game.games import Game


class FrogState:
    def __init__(self, board, to_move='L'):
        self.board = board
        self.to_move = to_move


class JumpingFrogGame(Game):
    def __init__(self, initial_state, player='MAX'):
        super(JumpingFrogGame, self).__init__(initial_state, player)
        self.initial_state = FrogState(board=initial_state, to_move='L')
        self.player = player

    def actions(self, state: FrogState):
        """
        Given a state return the list of possible actions
        @param state: a state of the game
        @return: a list
        """
        if state.to_move == 'L':
            possible_actions = [(i, i + 1) for i in range(len(state.board)) if state.board[i:i + 2] == ('L', '.')] + \
                               [(i, i + 2) for i in range(len(state.board)) if state.board[i:i + 3] == ('L', 'R', '.')]
        else:
            possible_actions = [(i + 1, i) for i in range(len(state.board)) if state.board[i:i + 2] == ('.', 'R')] + \
                               [(i + 2, i) for i in range(len(state.board)) if state.board[i:i + 3] == ('.', 'L', 'R')]

        return possible_actions

    def result(self, state: FrogState, action):
        """
        Given a state and an action returns the reached state
        @param state: a state of the game
        @param action: a possible action in the state
        @return: a new state
        """
        new_state = list(state.board)
        tmp = new_state[action[0]]
        new_state[action[0]] = new_state[action[1]]
        new_state[action[1]] = tmp
        return FrogState(board=tuple(new_state), to_move=self.next_to_move(state))

    def next_to_move(self, state: FrogState):
        to_move = state.to_move
        if state.to_move == 'R':
            to_move = 'L'
        else:
            to_move = 'R'
        return to_move

    def terminal_test(self, state: FrogState):
        """
        Returns True if the state is a final state (the game is over), False otherwise
        @param state: a state of the game
        @return: True or False
        """
        if state.board[len(state.board) // 2 + 1:] == ('L', 'L'):
            return True
        elif state.board[:len(state.board) // 2 - 1] == ('R', 'R'):
            return True
        elif not self.successors(state):
            return True
        return False

    def utility(self, state):
        """
        Given a state returns its utility
        @param state: a state of the game
        @return: a utility value (integer)
        """
        if self.terminal_test(state) and not self.successors(state):
            if state.to_move == 'L':
                return 1
            else:
                return -1
        return 0

    def display(self, state: FrogState):
        print('_____________________')
        print(self.player, 'in ', state.board)

    def display_move(self, state: FrogState, move):
        print(self.player, f'--{move}--> ', state.board)
