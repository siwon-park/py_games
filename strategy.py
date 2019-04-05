"""
A module for strategies.

NOTE: Make sure this file adheres to python-ta.
Adjust the type annotations as needed, and implement both a recursive
and an iterative version of minimax.
"""
import copy
from typing import Any
from game_state import GameState
from trees import Tree
from stack import Stack



def interactive_strategy(game: Any) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def rough_outcome_strategy(game: Any) -> Any:
    """
    Return a move for game by picking a move which results in a state with
    the lowest rough_outcome() for the opponent.

    NOTE: game.rough_outcome() should do the following:
        - For a state that's over, it returns the score for the current
          player of that state.
        - For a state that's not over:
            - If there is a move that results in the current player winning,
              return 1.
            - If all moves result in states where the other player can
              immediately win, return -1.
            - Otherwise; return a number between -1 and 1 corresponding to how
              'likely' the current player will win from the current state.

        In essence: rough_outcome() will only look 1 or 2 states ahead to
        'guess' the outcome of the game, but no further. It's better than
        random, but worse than minimax.
    """
    current_state = game.current_state
    best_move = None
    best_outcome = -2  # Temporarily -- just so we can replace this easily later

    # Get the move that results in the lowest rough_outcome for the opponent
    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(move)

        # We multiply the below by -1 since a state that's bad for the opponent
        # is good for us.
        guessed_score = new_state.rough_outcome() * -1
        if guessed_score > best_outcome:
            best_outcome = guessed_score
            best_move = move

    # Return the move that resulted in the best rough_outcome
    return best_move


def recursive_minimax_strategy(game: Any) -> Any:
    """
    Return a move that produces the highest guaranteed score at each step for
    the current player.
    For a game state that's over, the score is:
    1 - if the current player is the winner
    -1 - if the current player is the loser
    0 - if the game is a tie
    """

    moves = []

    current_state = game.current_state
    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(game.str_to_move(str(move)))
        moves.append(minimax_recursive_helper(game, new_state) * -1)
    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(game.str_to_move(str(move)))
        if minimax_recursive_helper(game, new_state) * -1 == \
                max(moves):
            return move
    return moves[0]


def minimax_recursive_helper(game: Any, state: GameState):
    """
    Helper function for recursive_minimax_strategy,
    returns the maximum score of a certain state.

    """
    old_game = copy.deepcopy(game)
    game.current_state = state
    if game.is_over(state):
        game.current_state = state
        if game.is_winner(state.get_current_player_name()):
            game.current_state = old_game.current_state
            return 1
        elif game.is_winner('p1') or game.is_winner('p2'):
            game.current_state = old_game.current_state
            return -1

        game.current_state = old_game.current_state
        return 0

    states = []
    for move in state.get_possible_moves():
        new_state = state.make_move(game.str_to_move(str(move)))
        states.append(new_state)
    return max([-1 * minimax_recursive_helper(game, x) for x in states])


def iterative_minimax_strategy(game: Any) -> Any:
    """
    Minimax strategy done with a tree file structure and stacks
    """
    old_game = copy.deepcopy(game)
    current_state = game.current_state
    root = Tree(current_state)
    stack = Stack()
    stack.add(root)
    while not stack.is_empty():
        top = stack.remove()
        game.current_state = top.value
        if game.is_over(top.value):
            game.current_state = top.value
            if game.is_winner(top.value.get_current_player_name()):
                top.score = 1
                game.current_state = old_game.current_state
            elif game.is_winner('p1') or game.is_winner('p2'):
                top.score = -1
                game.current_state = old_game.current_state
            else:
                top.score = 0
                game.current_state = old_game.current_state

        elif top.children == []:
            stack.add(top)
            for move in top.value.get_possible_moves():
                new_state = top.value.make_move(game.str_to_move(str(move)))
                trees = Tree(new_state)
                trees.move = move
                top.children.append(trees)
                stack.add(trees)
        else:
            children_score = []
            for child in top.children:
                children_score.append(child.score * -1)
            top.score = max(children_score)
    for child in root.children:
        if child.score * -1 == root.score:
            return child.move
    return old_game.current_state.get_possible_moves()[0]


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
