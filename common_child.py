def lowestCommonSequence(x, y):
    lengths = [[0 for j in range(len(y)+1)] for i in range(len(x)+1)]
    for i, x in enumerate(x):
        for j, y in enumerate(y):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])

    return lengths[-1][-1]

def main():
    s1 = raw_input()
    s2 = raw_input()
    print lowestCommonSequence(s1,s2)

main()