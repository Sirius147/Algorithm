import sys
input = sys.stdin.readline

def main():
    N,r,c = map(int, input().split())

    start, rIdx, cIdx = 0,0,0
    while N > 0:
        row,col = rIdx + (2**(N-1)), cIdx + (2**(N-1))
        if r < row and c < col:
            N -= 1
            continue
        elif r < row and c >= col:
            start = start + ((2**(N-1)) * (2**(N-1)))
            cIdx = col
        elif r >= row and c < col:
            start = start + ((2**(N-1)) * (2**(N-1))) * 2
            rIdx = row
        else:
            start = start + ((2**(N-1)) * (2**(N-1))) * 3
            rIdx, cIdx = row, col
        N -= 1
    print(start)




if __name__ == "__main__":
    main()