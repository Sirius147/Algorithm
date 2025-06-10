import sys

input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()

    visited = [False] * N
    permutations = []
    temp = []

    def DFS(cnt):
        if cnt == M:
            letters = " ".join(map(str,temp))
            permutations.append(letters)
            return
        
        for i in range(N):
            if visited[i] == False:
                visited[i] = True
                temp.append(nums[i])
                DFS(cnt+1)
                visited[i] = False
                temp.pop()      
    DFS(0)
    for i in permutations:
        print(i)


if __name__ == "__main__":
    solve()