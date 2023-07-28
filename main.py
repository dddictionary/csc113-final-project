from Board import Board
from Player import Player

def main():
    DIM = 4
    board = Board(DIM)
    player = Player(board)
    board.start()
    
    
if __name__ == '__main__':
    main()
