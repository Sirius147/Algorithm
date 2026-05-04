#import sys
from collections import deque

#sys.stdin = open("sample_input.txt", "r")


def function():
    # Use a breakpoint in the code line below to debug your script.
    T = int(input())
    for test_case in range(1, T + 1):
        E, N = map(int, input().split())
        nodes = [[] for _ in range(E + 2)]
        edges = list(map(int, input().split()))
        n = len(edges)
        for i in range(0, n - 1, 2):
            nodes[edges[i:i + 2][0]].append(edges[i:i + 2][1])

        q = deque()
        q.append(N)
        cnt = 1
        while q:
            idx = q.popleft()
            if len(nodes[idx]):
                q.extend(nodes[idx])
                cnt += len(nodes[idx])
        print(f"#{test_case} {cnt}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    function()