def rowIndex(n):
    row = [0] * (n+1)
    row[0] = 1
    for i in range(1, n+1):
        for j in range(i,0,-1):
            row[j] += row[j-1]
    return row

if __name__ == "__main__":
    print(rowIndex(4))
