import pygame as p
import chessEngine

p.init()
p.display.set_caption('CHESS')
g=chessEngine.game()
Width=600
Height=Width
screen = p.display.set_mode((Width,Height))

class chessboard():
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.dim=8
        self.size=self.height // self.dim
        self.images={}

    def loadImages(self):
        pieces=['bR','bN','bB','bK','bQ','bp','wp','wR','wN','wB','wK','wQ']
        for piece in pieces:
            self.images[piece]=p.transform.scale(p.image.load('IMAGES/'+piece+".png"),(self.size,self.size))
   
    def drawImages(self):
        for r in range(self.dim):
            for c in range(self.dim):
                piece=g.board[r][c]
                if piece !='--':
                    screen.blit(self.images[piece],p.Rect(c*self.size,r*self.size,self.size,self.size))
    
    def drawingboard(self):
        colors=[p.Color('white'),p.Color('gray')]
        screen.fill(p.Color("dark green"))
        for r in range(self.dim):
            for c in range(self.dim):
                color=colors[(r+c)%2]
                p.draw.rect(screen,color,p.Rect(r*self.size,c*self.size,self.size,self.size))

    def main(self): 
        chessboard.loadImages(self)
        clock=p.time.Clock()
        done = False
        Sqselected=()
        PlayerClicks=[]
        while not done:  
            for event in p.event.get():  
                if event.type == p.QUIT:  
                    done = True  
                elif event.type==p.MOUSEBUTTONDOWN:
                    loc=p.mouse.get_pos()
                    col=loc[0]//self.size
                    row=loc[1]//self.size
                    if Sqselected==(row,col):
                        Sqselected=()
                        PlayerClicks=[]
                    else:
                        Sqselected=(row,col)
                        PlayerClicks.append(Sqselected)
                    if len(PlayerClicks)==2:
                        move=chessEngine.move(PlayerClicks[0],PlayerClicks[1],g.board)
                        print(move.Notation())
                        g.MakeMove(move)
                        Sqselected=()
                        PlayerClicks=[]
                elif event.type==p.KEYDOWN:
                    if event.key ==p.K_z:
                        g.undoMove()
            clock.tick(15)
            chessboard.drawingboard(self)
            chessboard.drawImages(self)
            p.display.flip() 

q=chessboard(Width,Height)
q.main()