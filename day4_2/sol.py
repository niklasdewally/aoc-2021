INPUT = "input"
BOARD_WIDTH = 5


class Board:
    def __init__(self,values : [str] ):
        self.board = []
        self.bingo = False
        self.crossed = [[0 for i in range(BOARD_WIDTH)] for i in range(BOARD_WIDTH)]
        for row in range(BOARD_WIDTH):
            curr_row = []
            for col in range(BOARD_WIDTH):
                curr_row.append(values[row*BOARD_WIDTH + col])

            self.board.append(curr_row)

    def check_bingo(self):
        # row 
        for row in self.crossed:
            if sum(row) == BOARD_WIDTH:
                self.bingo = True
                return True
        # column
        for i in range(BOARD_WIDTH):
            if sum(row[i] for row in self.crossed) == BOARD_WIDTH:
                self.bingo = True
                return True
        return False


    def cross_num(self,n):
        self.crossed = [[1 if x==n else self.crossed[i][j] for j,x in enumerate(row)] for i,row in enumerate(self.board)]
        self.check_bingo()

    def __repr__(self):
        return str(self.board)



def parse_inputs(filename):
    bingonums = []   # List of input numbers
    bingoboards = [] # List of Board objects
    with open(filename) as f:
        # First line is bingonums
        firstline = next(f)
        bingonums = [int(x) for x in firstline.strip().split(",")]
        curr_board = []
        next(f) # skip blank line
        for i,line in enumerate(f):
            if line.strip() == "":
                # New board
                bingoboards.append(Board(curr_board))
                curr_board = []
                continue
            curr_board += [int(x) for x in line.strip().split(" ") if x != ""]

        # File doesnt end in a whitespace
        bingoboards.append(Board(curr_board))
    return bingonums,bingoboards


if __name__ == "__main__":
    nums,boards = parse_inputs(INPUT)
    i = 0
    while not boards[0].bingo or len(boards) > 1 :
        boards = [board for board in boards if not board.bingo]
        next_num = nums[i]
        for board in boards:
            board.cross_num(next_num)
        i+=1

    winningboard = boards[0]
    sumofunmarked = sum(sum(x if not winningboard.crossed[i][j] else 0 for j,x in enumerate(row)) for i,row in enumerate(winningboard.board))
    print(next_num*sumofunmarked)
