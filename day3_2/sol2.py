import numpy as np

INPUT = "input"

data = np.genfromtxt(INPUT,dtype="long",delimiter=1)
oxData = data.copy()

rows,cols = oxData.shape
i = 0
while rows > 1:
    
    sumofDigits = oxData[:,i].sum()
    if sumofDigits >= rows/2:
        target = 1
    else:
        target = 0
    
    # Filter column
    oxData = oxData[(oxData[:,i] == target)]
    rows,cols = oxData.shape
    i += 1

oxAnswer = int(np.array2string(oxData[0],separator="")[1:-1],2)


# CO2
co2Data = data.copy()
rows,cols = co2Data.shape
i = 0
while rows > 1:
    
    sumofDigits = co2Data[:,i].sum()
    if sumofDigits >= rows/2:
        target = 0
    else:
        target = 1
    
    # Filter column
    co2Data = co2Data[(co2Data[:,i] == target)]
    rows,cols = co2Data.shape
    i += 1

co2Answer = int(np.array2string(co2Data[0],separator="")[1:-1],2)

print(oxAnswer * co2Answer)
