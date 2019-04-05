"""
An implemntation of the game Stonehenge
This module contains the classes StonehengeGame and StonehengeState.
Both the classes are extended from the superclasses Game and GameState.
"""
import copy
from typing import Any
from game import Game
from game_state import GameState


class StonehengeGame(Game):
    """
    A class that is extended from superclass Game and is an abstract class
    for a game to be played with two players.
    """
    def __init__(self, p1_starts: bool) -> None:
        """
        Initialize this Game, using p1_starts to find who the first player is.
        """
        side_length = int(input("Enter the size of side_length: "))
        self.current_state = StonehengeState(p1_starts, side_length)
        self.win = ''

    def get_instructions(self) -> str:
        """
        Return the instructions for this Game.
        """
        instructions = "Players take turn claiming cells, when a player " \
                       "captures at least half of the cells in a ley-line, " \
                       "then the player captures that ley-line. The first " \
                       "person to capture at least half of the ley-lines " \
                       "is the winner."
        return instructions

    def is_over(self, state: "StonehengeState") -> bool:
        """
        Return whether or not this game is over at state.
        """
        counter_p1 = 0
        counter_p2 = 0
        for key in state.ll:
            if state.ll[key][0] == '1':
                counter_p1 += 1
            elif state.ll[key][0] == '2':
                counter_p2 += 1
        if counter_p1 >= 0.5 * len(state.ll) or \
                counter_p2 >= 0.5 * len(state.ll):
            return True
        return False

    def is_winner(self, player: str) -> bool:
        """
        Return whether player has won the game.

        Precondition: player is 'p1' or 'p2'.
        """

        return (self.current_state.get_current_player_name() != player
                and self.is_over(self.current_state))

    def str_to_move(self, string: str) -> Any:
        """
        Return the move that string represents. If string is not a move,
        return some invalid move.
        """
        return string


class StonehengeState(GameState):
    """
    A class that is extended from superclass GameState and describes the state
    of the game at a certain point in time.

    WIN - score if player is in a winning position
    LOSE - score if player is in a losing position
    DRAW - score if player is in a tied position
    p1_turn - whether it is p1's turn or not
    """
    WIN: int = 1
    LOSE: int = -1
    DRAW: int = 0
    p1_turn: bool

    def __init__(self, is_p1_turn: bool, side_length: int) -> None:
        """
        Initialize this game state and set the current player based on
        is_p1_turn.

        """
        self.p1_turn = is_p1_turn
        self.side_length = side_length
        self.board = ''

        if self.side_length == 1:
            self.ll = {'h1': ['@', 'A', 'B'],
                       'h2': ['@', 'C'],
                       'u1': ['@', 'A'],
                       'u2': ['@', 'B', 'C'],
                       'd1': ['@', 'C', 'A'],
                       'd2': ['@', 'B']}

        elif self.side_length == 2:
            self.ll = {'h1': ['@', 'A', 'B'],
                       'h2': ['@', 'C', 'D', 'E'],
                       'h3': ['@', 'F', 'G'],
                       'u1': ['@', 'A', 'C'],
                       'u2': ['@', 'B', 'D', 'F'],
                       'u3': ['@', 'E', 'G'],
                       'd1': ['@', 'F', 'C'],
                       'd2': ['@', 'G', 'D', 'A'],
                       'd3': ['@', 'E', 'B']}

        elif self.side_length == 3:
            self.ll = {'h1': ['@', 'A', 'B'],
                       'h2': ['@', 'C', 'D', 'E'],
                       'h3': ['@', 'F', 'G', 'H', 'I'],
                       'h4': ['@', 'J', 'K', 'L'],
                       'u1': ['@', 'A', 'C', 'F'],
                       'u2': ['@', 'B', 'D', 'G', 'J'],
                       'u3': ['@', 'E', 'H', 'K'],
                       'u4': ['@', 'I', 'L'],
                       'd1': ['@', 'J', 'F'],
                       'd2': ['@', 'K', 'G', 'C'],
                       'd3': ['@', 'L', 'H', 'D', 'A'],
                       'd4': ['@', 'I', 'E', 'B']}

        elif self.side_length == 4:
            self.ll = {'h1': ['@', 'A', 'B'],
                       'h2': ['@', 'C', 'D', 'E'],
                       'h3': ['@', 'F', 'G', 'H', 'I'],
                       'h4': ['@', 'J', 'K', 'L', 'M', 'N'],
                       'h5': ['@', 'O', 'P', 'Q', 'R'],
                       'u1': ['@', 'A', 'C', 'F', 'J'],
                       'u2': ['@', 'B', 'D', 'G', 'K', 'O'],
                       'u3': ['@', 'E', 'H', 'L', 'P'],
                       'u4': ['@', 'I', 'M', 'Q'],
                       'u5': ['@', 'N', 'R'],
                       'd1': ['@', 'O', 'J'],
                       'd2': ['@', 'P', 'K', 'F'],
                       'd3': ['@', 'Q', 'L', 'G', 'C'],
                       'd4': ['@', 'R', 'M', 'H', 'D', 'A'],
                       'd5': ['@', 'N', 'I', 'E', 'B']}

        elif self.side_length == 5:
            self.ll = {'h1': ['@', 'A', 'B'],
                       'h2': ['@', 'C', 'D', 'E'],
                       'h3': ['@', 'F', 'G', 'H', 'I'],
                       'h4': ['@', 'J', 'K', 'L', 'M', 'N'],
                       'h5': ['@', 'O', 'P', 'Q', 'R', 'S', 'T'],
                       'h6': ['@', 'U', 'V', 'W', 'X', 'Y'],
                       'u1': ['@', 'A', 'C', 'F', 'J', 'O'],
                       'u2': ['@', 'B', 'D', 'G', 'K', 'P', 'U'],
                       'u3': ['@', 'E', 'H', 'L', 'P', 'V'],
                       'u4': ['@', 'I', 'M', 'R', 'W'],
                       'u5': ['@', 'N', 'S', 'X'],
                       'u6': ['@', 'T', 'Y'],
                       'd1': ['@', 'U', 'O'],
                       'd2': ['@', 'V', 'P', 'J'],
                       'd3': ['@', 'W', 'Q', 'K', 'F'],
                       'd4': ['@', 'X', 'R', 'L', 'G', 'C'],
                       'd5': ['@', 'Y', 'S', 'M', 'H', 'D', 'A'],
                       'd6': ['@', 'T', 'N', 'I', 'E', 'B']}

    def __str__(self) -> str:
        """
        Return a string representation of the current state of the game.
        """

        if self.side_length == 1:

            self.board = """\
      {0[u1][0]}   {0[u2][0]}
     /   /
{0[h1][0]} - {0[h1][1]} - {0[h1][2]}
     \\ / \\
  {0[h2][0]} - {0[h2][1]}   {0[d2][0]}
       \\
        {0[d1][0]}""".format(self.ll)

        elif self.side_length == 2:

            self.board = """\
        {0[u1][0]}   {0[u2][0]}
       /   /
  {0[h1][0]} - {0[h1][1]} - {0[h1][2]}   {0[u3][0]}
     / \\ / \\ /
{0[h2][0]} - {0[h2][1]} - {0[h2][2]} - {0[h2][3]}
     \\ / \\ / \\
  {0[h3][0]} - {0[h3][1]} - {0[h3][2]}   {0[d3][0]}
       \\   \\
        {0[d1][0]}   {0[d2][0]}""".format(self.ll)

        elif self.side_length == 3:

            self.board = """\
          {0[u1][0]}   {0[u2][0]}
         /   /
    {0[h1][0]} - {0[h1][1]} - {0[h1][2]}   {0[u3][0]}
       / \\ / \\ /
  {0[h2][0]} - {0[h2][1]} - {0[h2][2]} - {0[h2][3]}   {0[u4][0]}
     / \\ / \\ / \\ /
{0[h3][0]} - {0[h3][1]} - {0[h3][2]} - {0[h3][3]} - {0[h3][4]}
     \\ / \\ / \\ / \\
  {0[h4][0]} - {0[h4][1]} - {0[h4][2]} - {0[h4][3]}   {0[d4][0]}
       \\   \\   \\ 
        {0[d1][0]}   {0[d2][0]}   {0[d3][0]}""".format(self.ll)

        elif self.side_length == 4:

            self.board = """\
            {0[u1][0]}   {0[u2][0]}
           /   /
      {0[h1][0]} - {0[h1][1]} - {0[h1][2]}   {0[u3][0]}
         / \\ / \\ /
    {0[h2][0]} - {0[h2][1]} - {0[h2][2]} - {0[h2][3]}   {0[u4][0]}
       / \\ / \\ / \\ /
  {0[h3][0]} - {0[h3][1]} - {0[h3][2]} - {0[h3][3]} - {0[h3][4]} \
  {0[u5][0]}
     / \\ / \\ / \\ / \\ / 
{0[h4][0]} - {0[h4][1]} - {0[h4][2]} - {0[h4][3]} - {0[h4][4]} - {0[h4][5]}
     \\ / \\ / \\ / \\ / \\
  {0[h5][0]} - {0[h5][1]} - {0[h5][2]} - {0[h5][3]} - {0[h5][4]}   {0[d5][0]}
       \\   \\   \\   \\
        {0[d1][0]}   {0[d2][0]}   {0[d3][0]}   {0[d4][0]}""".format(self.ll)

        elif self.side_length == 5:

            self.board = """\
              {0[u1][0]}   {0[u2][0]}
             /   /
        {0[h1][0]} - {0[h1][1]} - {0[h1][2]}   {0[u3][0]}
           / \\ / \\ /
      {0[h2][0]} - {0[h2][1]} - {0[h2][2]} - {0[h2][3]}   {0[u4][0]}
         / \\ / \\ / \\ /
    {0[h3][0]} - {0[h3][1]} - {0[h3][2]} - {0[h3][3]} - {0[h3][4]}   {0[u5][0]}
       / \\ / \\ / \\ / \\ / 
  {0[h4][0]} - {0[h4][1]} - {0[h4][2]} - {0[h4][3]} - {0[h4][4]} - {0[h4][5]}  \
 {0[u6][0]}   
     / \\ / \\ / \\ / \\ / \\ /
{0[h5][0]} - {0[h5][1]} - {0[h5][2]} - {0[h5][3]} - {0[h5][4]} - {0[h5][5]} - \
{0[h5][6]}   
     \\ / \\ / \\ / \\ / \\ / \\
  {0[h6][0]} - {0[h6][1]} - {0[h6][2]} - {0[h6][3]} - {0[h6][4]} - {0[h6][5]} \
  {0[d6][0]}
       \\   \\   \\   \\   \\
        {0[d1][0]}   {0[d2][0]}   {0[d3][0]}   {0[d4][0]}   {0[d5][0]}""".\
                format(self.ll)
        return self.board

    def get_possible_moves(self) -> list:
        """
        Return all possible moves that can be applied to this state.
        """
        possible_moves = []
        counter_p1 = 0
        counter_p2 = 0
        for key in self.ll:
            if self.ll[key][0] == '1':
                counter_p1 += 1
            elif self.ll[key][0] == '2':
                counter_p2 += 1
        if counter_p1 < 0.5 * len(self.ll) and counter_p2 < 0.5 * len(self.ll):
            for key in self.ll:
                for value in self.ll[key]:
                    self.append_values(possible_moves, value)
        return possible_moves

    def append_values(self, possible_moves: list, value: str):
        """
        Helper function to append the values in the key to possible_moves for
        get_possible_moves
        """
        if value not in '@, 1, 2' and value not in possible_moves:
            possible_moves.append(value)

    def get_current_player_name(self) -> str:
        """
        Return 'p1' if the current player is Player 1, and 'p2' if the current
        player is Player 2.
        """
        if self.p1_turn:
            return 'p1'
        return 'p2'

    def make_move(self, move: Any) -> 'GameState':
        """
        Return the GameState that results from applying move to this GameState.
        """
        new_state = copy.deepcopy(self)
        if new_state.get_current_player_name() == 'p1':
            n = '1'
        else:
            n = '2'
        for key in new_state.ll:
            for index in range(len(new_state.ll[key])):
                if move == new_state.ll[key][index]:
                    new_state.ll[key][index] = n
        for key in new_state.ll:
            if new_state.ll[key][0] not in '1, 2' and \
                    new_state.ll[key].count(n) \
                    >= 0.5 * (len(new_state.ll[key]) - 1):
                new_state.ll[key][0] = n
        new_state.p1_turn = not self.p1_turn
        return new_state

    def is_valid_move(self, move: Any) -> bool:
        """
        Return whether move is a valid move for this GameState.
        """
        return move in self.get_possible_moves()

    def __repr__(self) -> Any:
        """
        Return a representation of this state (which can be used for
        equality testing).
        """
        return self.board + " \n Current Player Name: " + self.\
            get_current_player_name()

    def rough_outcome(self) -> float:
        """
        Return an estimate in interval [LOSE, WIN] of best outcome the current
        player can guarantee from state self.
        """
        counter_p1 = 0
        counter_p2 = 0
        for key in self.ll:
            if self.ll[key][0] == '1':
                counter_p1 += 1
            elif self.ll[key][0] == '2':
                counter_p2 += 1
        if self.get_current_player_name() == 'p1':
            if counter_p1 >= 0.5 * len(self.ll) or counter_p2 < counter_p1:
                return 1
            elif counter_p2 > 0.5 * len(self.ll) - 1:
                return -1
        elif self.get_current_player_name() == 'p2':
            if counter_p2 >= 0.5 * len(self.ll) or counter_p1 < counter_p2:
                return 1
            elif counter_p1 > 0.5 * len(self.ll) - 1:
                return -1
        return 0


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
