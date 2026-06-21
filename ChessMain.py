import pygame as p
import ChessEngine #imports ChessEngine.py 

WIDTH = HEIGHT = 512 #dimensions of board
DIMENSION = 8 # 8 x 8
SQ_SIZE = HEIGHT // DIMENSION #one square size
MAX_FPS = 15 #setting max fps to 15
IMAGES = {}  # array for chess pieces (images)

def loadImages():
    pieces = ['bB', 'bK', 'bN', 'bp', 'bQ', 'bR', 'wB', 'wK', 'wN', 'wp', 'wQ', 'wR']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load('assets/' + piece + '.png'), (SQ_SIZE, SQ_SIZE))
#this function loads pieces only call one time
def main():
    p.init()
    #loads board, pieces
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color('white'))
    gs = ChessEngine.GameState()
    
    validMoves = gs.getValidMoves()
    moveMode = False #flag variable when move is made
    
    loadImages()
    running = True
    sqSelected = () #no squares selected, keep track of last click of the user (tuple: row, column)
    playerClicks = [] #list (keep track of player clicks) two tuples: [(6, 4), (4, 4)]

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            #mouse hander
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() #this is x y location of mouse
                col = location[0] // SQ_SIZE 
                row = location[1] // SQ_SIZE
                if(sqSelected == (row, col)): #undo action (user clicked on same row & col)
                    sqSelected = () #unselect
                    playerClicks = []
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected) #append for both first and second click
                #was that users second click

                if(len(playerClicks) == 2): #after 2nd click
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    if move in validMoves:
                        gs.makeMove(move)
                        moveMode = True
                        sqSelected = () #reset user clicks
                        playerClicks = []
                    else:
                        playerClicks = [sqSelected]
            #key hander
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:
                    gs.undoMove()
                    moveMode = True

        if moveMode:
            validMoves = gs.getValidMoves()
            moveMode = False
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

def drawGameState(screen, gs): #draws board & pieces
    drawBoard(screen) 
    drawPieces(screen, gs.board) 

def drawBoard(screen): 
    colors = [p.Color('white'), p.Color('gray')]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)] 
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != '--':
                screen.blit(IMAGES[piece], p.Rect((c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE)))

if __name__ == '__main__':
    main()