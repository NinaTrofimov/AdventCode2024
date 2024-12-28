with open('input.txt', 'r') as file:
    inputdata = file.readlines('\n')

print(inputdata)

value1 = []
value2 = []
for line in inputdata:
    line = line.split()
    list1 = []
    list2 = []
    for i in range(13):
        while i <= 6:
          list1.append(inputdata[i])
        else:
          list2.append(inputdata[i])
    value1 = list1.sort()
    value2 = list2.sort()
    print(line)