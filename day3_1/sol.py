NUM_SIZE = 12  
ones = [0 for i in range(NUM_SIZE)]
zeros = [0 for i in range(NUM_SIZE)]

# Compute number of 1s and 0s
with open("input") as f:
    for line in f:
        for i in range(0,NUM_SIZE):
            if (line[i] == "1"):
                ones[i] += 1;
            else:
                zeros[i] += 1;

# Compute gamma and epsilon
gamma = 0
epsilon = 0 
for i in range(NUM_SIZE):
    gamma <<= 1
    epsilon <<= 1
    if (ones[i] > zeros[i]):
        gamma += 1;
    else:
        epsilon +=1;

print(gamma*epsilon)
