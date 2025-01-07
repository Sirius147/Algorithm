import sys
input = sys.stdin.readline


def solve():
    N = int(input())
    list1 = []
    
    for _ in range(N):
        list1.append(list(map(int,input().split())))
    
    for i in range(1,N):
        list1[i][0] += min(list1[i-1][1], list1[i-1][2])
        list1[i][1] += min(list1[i-1][0], list1[i-1][2])
        list1[i][2] += min(list1[i-1][0], list1[i-1][1])
    
    print(min(list1[N-1]))
        
if __name__ == "__main__":
    solve()
        

