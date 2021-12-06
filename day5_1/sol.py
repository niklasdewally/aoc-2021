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

        if (y-y1 == 0):
            # Horizontal
            lower_x = x if x<x1 else x1
            higher_x = x1 if x<x1 else x
            
            for coord in range(lower_x,higher_x+1):
                grid[coord][y] += 1

        elif (x-x1 == 0):
            lower_y = y if y<y1 else y1
            higher_y = y1 if y<y1 else y

            for coord in range(lower_y,higher_y+1):
                grid[x][coord] +=1
        
    #print([1 for row in grid for item in row if item > 1])
    print(sum(1 for row in grid for item in row if item > 1))

