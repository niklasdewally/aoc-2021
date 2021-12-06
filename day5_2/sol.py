def parse_input(filename):
    with open(filename) as f:
        data = []
        for line in f:
            data.append([[int(a) for a in e.strip().split(",")] for e in line.split("->")])
    return data


if __name__ == "__main__":
    data = parse_input("input")
    size = max([coord for line in data for items in line for coord in items]) + 1 # 0 indexed
    grid = [ [0 for i in range(size)] for j in range(size)]

    for (x,y),(x1,y1) in data:

        lower_y = y if y<y1 else y1
        higher_y = y1 if y<y1 else y
        lower_x = x if x<x1 else x1
        higher_x = x1 if x<x1 else x

        if (y-y1 == 0):
            # Horizontal
            for coord in range(lower_x,higher_x+1):
                grid[y][coord] += 1

        elif (x-x1 == 0):
            for coord in range(lower_y,higher_y+1):
                grid[coord][x] += 1

        elif (higher_x-lower_x) == (higher_y-lower_y): # Diagonal
            xdir = 1 if (x1-x) > 0 else -1
            ydir = 1 if (y1-y) > 0 else -1
            for i in range(0,(higher_x-lower_x)+1):
                grid[y + i*ydir][x + i*xdir] += 1
        
    for l in grid:
        print(l)
    #print([1 for row in grid for item in row if item > 1])
    print(sum(1 for row in grid for item in row if item > 1))

