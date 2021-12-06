GENERATIONS = 256
INPUT = 'input'

def parse_input(filename):
    with open(filename) as f:
        return [int(x) for x in f.read().strip().split(",")]



fish = parse_input(INPUT)
#print("Day 0:",fish)
for day in range(1,GENERATIONS+1):
    toadd = sum(1 for x in fish if x == 0)
    fish = [x-1 if x>0 else 6 for x in fish ]
    fish.extend(8 for i in range(0,toadd))
 #   print("Day",day,fish)

print(len(fish))
