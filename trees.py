"""
Module trees to be used for the minimax iterative strategy.
taken from lab
"""


class Tree:
    """
    A bare-bones Tree ADT that identifies the root with the entire tree.
    """

    def __init__(self, value=None, children=None) -> None:
        """
        Create Tree self with content value and  0 or more children
        """
        self.value = value
        # copy children if not None
        self.children = children[:] if children is not None else []
        self.score = None
        self.move = None


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
