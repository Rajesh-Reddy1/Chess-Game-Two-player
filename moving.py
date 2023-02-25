import chessEngine
g = chessEngine.game()
n=chessEngine.notations

def validmoves():
    moves = []
    for r in range(len(g.board)):
        for c in range(len(g.board[r])):
            turn = g.board[r][c][0]
            if (turn == 'w' and g.whiteToMove) or (turn == 'b' and not g.whiteToMove):
                piece = g.board[r][c][1]
                if piece == 'p':
                    PawnMoves(r,c,moves)
    return moves

def PawnMoves( r , c ,moves):
    if g.whiteToMove:
        if g.board[r-1][c]=='--':
            moves.append(n((r,c),(r-1,c),g.board))
            if r==6 and g.board[r-2][c]=='--':
                moves.append(n((r,c),(r-2,c),g.board))

def RookMoves(r , c ,moves):
    pass

def KnightMoves(r , c ,moves):
    pass

def BishopMoves(r , c ,moves):
    pass

def KingMoves(r , c ,moves):
    pass

def QueenMoves(r , c ,moves):
    pass