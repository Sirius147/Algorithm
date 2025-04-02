import sys
input = sys.stdin.readline
from collections import deque

def solve():
    N = int(input())

    adjMatrix = [list(map(int,input().split())) for _ in range(N)]
    visited = [False] * N

    edgeDict = {i:[] for i in range(N)}

    for i in range(N):
        for j in range(N):
            if adjMatrix[i][j] == 1: edgeDict[i].append(j)

    routeQ = deque()

    for i in range(N):
        routeQ.extend(edgeDict[i])
        while routeQ:
            nextNodeIdx = routeQ.popleft()
            if visited[nextNodeIdx]: continue

            visited[nextNodeIdx] = True
            adjMatrix[i][nextNodeIdx] = 1
            routeQ.extend(edgeDict[nextNodeIdx])

        for j in range(N): visited[j] = False
    # 노드 별로 경로 판단
    # 진행방식: 노드 엣지 정보 파악
        # 최초 q에서 진행 -> 새 노드 방문 시 q 갱신
        # 새 노드 방문 -> 엣지에서 정보 제공 (노드별로 진행 노드 인덱스 -> 엣지의 값)
        # 노드 엣지 정보 관리 자료 구조 -> dict (key는 노드 번호, value는 엣지 리스트)
    # cond1: 방문했던 노드 재방문 종료
    # cond2: 본 노드로 돌아오면 종료
    # cond3: 더 이상 진행할 노드가 없으면 종료
    for i in range(N):
        for j in range(N):
            print(adjMatrix[i][j], end=' ')
        print()



if __name__ == "__main__":
    solve()