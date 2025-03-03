import sys
input = sys.stdin.readline


def solve():
    # step 별로 이전 회의 종료 시간 이후 시작하는 회의 찾기
    # 해당 회의들 중 종료시간이 가장 이른 회의 찾고 cnt up
    # 이후 step 별로 반복

    cnt = 0
    endTime = 0
    N = int(input())

    meetings = [list(map(int,input().split())) for _ in range(N)]
    meetings.sort(key = lambda x: (x[1],x[0]))


    for meeting in meetings:
        if endTime <= meeting[0]:
            cnt += 1; endTime = meeting[1]
    
    print(cnt)


if __name__ == "__main__":

    solve()

