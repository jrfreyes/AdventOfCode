import numpy as np

class BingoBoard:
    def __init__(self, numbers) -> None:
        self.board = np.array(numbers)
        self.marked = np.zeros_like(self.board)
        self.last_draw = 0

    def is_winning(self) -> bool:
        return np.any([
            np.apply_along_axis(np.all, axis=0, arr=self.marked).any(),
            np.apply_along_axis(np.all, axis=1, arr=self.marked).any()
            ])
    
    def draw(self, num) -> None:
        self.marked[self.board==num] = 1
        self.last_draw = num

    def get_score(self) -> int:
        return self.board[self.marked==0].sum() * self.last_draw

class BingoGame:
    def __init__(self, filename) -> None:
        with open(filename) as f:
            self.draws = [int(x.strip()) for x in f.readline().split(',')]
            f.readline()
            boards = f.read().strip().split('\n\n')
        
        boards = [[[
            int(x) for x in row.strip().split()] 
                    for row in board.split('\n')] 
                    for board in boards]
        self.boards = {i : BingoBoard(board) for i, board in enumerate(boards)}
    
        self.finished = False
        self.score = 0
        self.last_draw = None

    def play(self):
        for draw in self.draws:
            self.last_draw = draw
            for i in self.boards:
                board = self.boards[i]
                board.draw(draw)
                if board.is_winning():
                    self.finished = True
                    self.score = board.get_score()
                    break
            if self.finished:
                break
    
    def playtwo(self):
        for draw in self.draws:
            self.last_draw = draw
            
            for i in self.boards.copy():
                board = self.boards[i]
                board.draw(draw)
                if board.is_winning():
                    if len(self.boards) > 1:
                        self.boards.pop(i)
                    else:    
                        self.finished = True
                        self.score = board.get_score()
                        break
            if self.finished:
                break
            




def main():
    game = BingoGame('input.txt')
    game.play()
    print(game.score)
    game2 = BingoGame('input.txt')
    game2.playtwo()
    print(game2.score, game2.last_draw)
    

if __name__ == '__main__':
    main()
