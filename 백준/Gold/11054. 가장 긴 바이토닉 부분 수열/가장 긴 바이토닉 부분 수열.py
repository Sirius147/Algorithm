import sys
input = sys.stdin.readline

def main():
    
    N = int(input())
    seq = list(map(int,input().split()))
    reverse = seq[::-1]

    increasing = [1]*N
    decreasing = [1]*N

    for i in range(N):
        for j in range(i):
            if seq[i] > seq[j]:
                increasing[i] = max(increasing[j]+1, increasing[i])

    for i in range(N):
        for j in range(i):
            if reverse[i] > reverse[j]:
                decreasing[i] = max(decreasing[i], decreasing[j] + 1)

    result = [0]*N
    decreasing = decreasing[::-1]
    for i in range(N):
        result[i] = increasing[i] + decreasing[i] - 1
    
    print(max(result))


if __name__ == "__main__":
    main()