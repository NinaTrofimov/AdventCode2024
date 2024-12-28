with open('input.txt', 'r') as file:
    sequences = [list(map(int, line.split())) for line in file if line.strip()]
safecounter = 0

for num in sequences:
    isSequenceSafe = False

    for i in range(len(num)):
        modified_num = num[:i] + num[i + 1:]
        isSafe = True
        increase = 0
        decrease = 0

        for j in range(len(modified_num) - 1):
            difference = abs(modified_num[j] - modified_num[j + 1])
            if difference in {1, 2, 3}:
                if modified_num[j] < modified_num[j + 1]:
                    increase += 1
                elif modified_num[j] > modified_num[j + 1]:
                    decrease += 1
            else:
                isSafe = False
                break


        if isSafe and (increase == 0 or decrease == 0):
            isSequenceSafe = True
            break
    if isSequenceSafe:
        print("Safe")
        safecounter += 1
    else:
        print("Unsafe")
print(safecounter)