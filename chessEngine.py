

class game():
    def __init__(self):
        self.board=[
            ['bR','bN','bB','bQ','bK','bB','bN','bR'],
            ['bp','bp','bp','bp','bp','bp','bp','bp'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['wp','wp','wp','wp','wp','wp','wp','wp'],
            ['wR','wN','wB','wQ','wK','wB','wN','wR']]
        self.whiteToMove=True
        self.moveLog=[]

    def MakeMove(self,move):
        self.board[move.StartRow][move.StartCol]="--"
        self.board[move.EndRow][move.EndCol]=move.pieceMoved
        self.moveLog.append(move)
        self.whiteToMove=not self.whiteToMove
    
    def undoMove(self):
        if len(self.moveLog)!=0:
            move=self.moveLog.pop()
            self.board[move.StartRow][move.StartCol]=move.pieceMoved
            self.board[move.EndRow][move.EndCol]=move.pieceCaptured
            self.whiteToMove=not self.whiteToMove


class move():
    #Board values
    Rows={"1":7,"2":6,"3":5,"4":4,"5":3,"6":2,"7":1,"8":0} 
    rowsvalue={v:k for k,v in Rows.items()}
    Cols={"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7}
    Colsvalue={v:k for k,v in Cols.items()}
    
    def __init__(self,StartSq,EndSq,board):
        self.StartRow=StartSq[0]
        self.StartCol=StartSq[1]
        self.EndRow=EndSq[0]
        self.EndCol=EndSq[1]
        self.pieceMoved=board[self.StartRow][self.StartCol]
        self.pieceCaptured=board[self.EndRow][self.EndCol]
    
    def Notation(self):
        return self.getRankFile(self.StartRow,self.StartCol)+" "+self.getRankFile(self.EndRow,self.EndCol)
    
    def getRankFile(self,r,c):
        return self.Colsvalue[c] +"-"+ self.rowsvalue[r]