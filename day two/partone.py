

with open('input.txt', 'r') as file:
    sequences = [list(map(int, line.split())) for line in file if line.strip()]
print(sequences)
safecount = 0
for num in sequences:
    increase = 0
    decrease = 0
    equal = 0
    for i in range(len(num)-1):
        difference = abs(num[i] - num[i+1])
        if num[i] > num[i+1] and difference in {1,2,3}:
            decrease += 1
        elif num[i] < num[i+1] and difference in {1,2,3}:
            increase += 1
        else: 
            equal += 1

    if equal == 0:
        if increase == 0 or decrease == 0:
            print('Safe')
            safecount += 1
        else:
            print('Unsafe')
    else:
        print('Unsafe')
print(safecount)