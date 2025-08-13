import sys
import heapq
from math import inf
input = sys.stdin.readline

def solve():

    nn = int(input())
    en = int(input())
    distances = [inf] * (nn + 1)
    graph = [[] for i in range(nn+1)]

    for _ in range(en):
        s,e,c = map(int, input().split())
        graph[s].append((e,c))
    
    start, target = map(int, input().split())
    distances[start] = 0
    q = []
    heapq.heappush(q,[distances[start], start])

    while q:
        currDist, currPoint = heapq.heappop(q)
        if currDist > distances[currPoint]: continue    # 이미 다른 엣지 등으로 갱신 되어 있는 노드 탐색 정보

        for e,c in graph[currPoint]:

            if currDist + c < distances[e]:
                distances[e] = currDist + c
                heapq.heappush(q,[currDist + c, e])
    
    print(distances[target])

if __name__ == "__main__":
    solve()

