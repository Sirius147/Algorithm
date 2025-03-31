import sys
import heapq
input = sys.stdin.readline

def solve():
    plusHeap = []
    minusHeap = []

    t = int(input())
    for _ in range(t):
        a = int(input())
        if a == 0:
            if minusHeap and plusHeap:
                p = heapq.heappop(plusHeap)
                m = -heapq.heappop(minusHeap)
                if abs(p) < abs(m):
                    print(p)
                    heapq.heappush(minusHeap,-m)
                else: 
                    print(m)
                    heapq.heappush(plusHeap,p)
            else:
                if minusHeap and not plusHeap:
                    print(-heapq.heappop(minusHeap))
                elif plusHeap and not minusHeap:
                    print(heapq.heappop(plusHeap))
                else: print(0)
        else:
            if a > 0: heapq.heappush(plusHeap, a)
            else: heapq.heappush(minusHeap, -a)

if __name__ == "__main__":
    solve()
