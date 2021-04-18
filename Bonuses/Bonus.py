class Diagonal:
    def __init__(self):
        self.tuples = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    @staticmethod
    def get_pieces():
        return ["knight", "rook"]

    @staticmethod
    def get_name():
        return ["Diagonal Upgrade: 1", "Gives a piece the ability to move like a bishop"]


class Horizontal:
    def __init__(self):
        self.tuples = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    @staticmethod
    def get_pieces():
        return ["knight", "bishop"]

    @staticmethod
    def get_name():
        return ["Straight Upgrade: 2", "Gives a piece the ability to move like a rook"]


class Knighted:
    def __init__(self):
        self.tuples = [(-2, -1), (-1, -2), (1, 2), (2, 1),
                       (-1, 2), (-2, 1), (2, -1), (1, -2)]

    @staticmethod
    def get_pieces():
        return ["king", "queen", "rook", "bishop"]

    @staticmethod
    def get_name():
        return ["Knighted Upgrade: 3", "Gives a piece the ability to move like a knight"]
