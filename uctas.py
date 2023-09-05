
class UcTas():
    def __init__(self):
        self.board = [["_", "_", "_"],
                      ["_", "_", "_"],
                      ["_", "_", "_"]]
        self.turn = "b"
        self.num_played_moves = 0

    def __repr__(self):
        return "\n".join(map(repr, self.board))

    def is_move_possible(self, piece, move):

        return (



            (self.board[move[0]][move[1]] == "_" or self.board[move[0]][move[1]]==self.turn) and

                (abs(move[0] - piece[0]) + abs(move[1] - piece[1]) == 1 and
                              self.board[piece[0]][piece[1]] == self.turn)
        )

    def play_move(self, piece, move):
        self.board[move[0]][move[1]] = self.turn
        if piece:
            self.board[piece[0]][piece[1]] = "_"
        self.num_played_moves += 1
        self.turn = "b" if self.turn == "s" else "s"

    def undo_move(self, piece, move):
        self.turn = "b" if self.turn == "s" else "s"
        self.num_played_moves -= 1
        if piece:
            self.board[piece[0]][piece[1]] = self.turn
        self.board[move[0]][move[1]] = "_"

    def winner(self):
        columns = [[self.board[0][0], self.board[1][0], self.board[2][0]],
                   [self.board[0][1], self.board[1][1], self.board[2][1]],
                   [self.board[0][2], self.board[1][2], self.board[2][2]]]
        for lines in (columns, self.board):
            for line in lines:
                if "".join(line) in ("bbb", "sss"):
                    return line[0]

        return False

    def actions(self):
        moves = []
        for i, row in enumerate(self.board):
            for j, content in enumerate(row):
                if content == "_":
                    moves.append((None, (i, j)))
        if self.num_played_moves >= 6:
            targets = moves
            moves = []
            for i, row in enumerate(self.board):
                for j, content in enumerate(row):
                    if content == self.turn:
                        piece = (i, j)
                        for _, move in targets:
                            if self.is_move_possible(piece, move):
                                moves.append((piece, move))
        return moves

    def utility(self):
        win = self.winner()
        if win == "s":
            return 100
        if win == "b":
            return -100
        return 0

    def minimax(self, depth):
        best_move = None
        best_score = self.utility()
        if best_score == 0 and depth > 0:
            optimal = (min, max)[self.turn == "s"]
            best_score = -optimal(-float("inf"), float("inf"))
            for piece, move in self.actions():
                self.play_move(piece, move)
                score = self.minimax(depth - 1)[0]  # extract score
                if optimal(best_score, score) != best_score:
                    best_score = score
                    best_move = (piece, move)
                self.undo_move(piece, move)

        return best_score, best_move





