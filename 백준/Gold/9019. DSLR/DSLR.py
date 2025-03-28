import sys
from collections import deque
input = sys.stdin.readline  

def solve(A:int, B:int):
    q = deque()
    q.append((A,''))
    # 목표 노드로 가는 방법은 꼭 직선적이지 않다 상태별로 다르다
    # 방문할 수 있는 노드를 확인한다
    # 새로 방문한 노드에 경로를 저장한다
    # dequeue 안에 방문 예정인 노드를 관리한다
    # 방문한 노드는 다시 방문하지 않는다 -> 메모리 관리 효율
    # 시간 복잡도는 내려놓는다
    visited = [False] * 10001
    visited[A] = True
    while q:
        num, cmd = q.popleft()
        if num == B:
            print(cmd)
            return
        D = num * 2
        if D > 9999: D %= 10000
        if not visited[D]:
            visited[D] = True
            q.append((D,cmd + 'D'))
        S = num - 1
        if S < 0: S = 9999
        if not visited[S]:
            visited[S] = True
            q.append((S,cmd + 'S'))
        L = ((num * 10) % 10000 + (num * 10) // 10000)
        if not visited[L]:
            visited[L] = True
            q.append((L,cmd + 'L'))
        R = ((num // 10)) + (num % 10) * 1000
        if not visited[R]:
            visited[R] = True
            q.append((R,cmd + 'R'))





if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        A,B = map(int, input().split())
        solve(A,B)