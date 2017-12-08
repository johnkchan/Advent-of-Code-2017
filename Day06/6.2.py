key = "4	1	15	12	0	9	9	5	5	8	7	3	14	5	12	3"
key = [int(i) for i in key.split("\t")]

container = []
conditionMet = False

while not conditionMet:
    maxValue = max(key)
    maxIndex = key.index(maxValue)

    key[maxIndex] = 0
    for i in range(maxIndex + 1, maxIndex + maxValue + 1):
        key[i % len(key)] += 1

    if key not in container:
        container.append(key[:])
    else:
        conditionMet = True
        print(len(container) - container.index(key))
