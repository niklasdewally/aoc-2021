GENERATIONS = 256
INPUT = 'input'

def parse_input(filename):
    fish = [0 for i in range(0,9)]
    print(fish)
    with open(filename) as f:
        for line in f:
            for a in line.strip().split(","):
                fish[int(a)] += 1
    return fish


fish = parse_input(INPUT)
print("Day 0:",fish)
for day in range(1,GENERATIONS+1):
    print("Day",day,fish)
    old0 = fish[0]
    fish[0] = fish[1]
    fish[1] = fish[2]
    fish[2] = fish[3]
    fish[3] = fish[4]
    fish[4] = fish[5]
    fish[5] = fish[6]
    fish[6] = fish[7] + old0
    fish[7] = fish[8]
    fish[8] = old0

print(sum(fish))

