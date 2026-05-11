from collections import deque

# sys.stdin = open("sample_input.txt", "r")


def function():
    # T 입력받고 루프 생성
    # 루프 별로 길이 N 입력받기
    # N길이의 상태리스트 생성
    # A팀, B팀 선호리스트 입력받기
    # A팀, B팀 표시용 리스트생성
    # aflag, bflag일 때 영입 or 영입가능한 선수 없을 때까지 영입시도하기
    # 차례 종료 후, flag변경
    T = int(input())
    for _ in range(T):
        N = int(input())
        players = [True for _ in range(N)]
        teamA = deque(map(int, input().split()))
        teamB = deque(map(int, input().split()))
        final = ['' for _ in range(N)]
        aflag, bflag = True, False

        while teamA or teamB:
            if aflag:
                while teamA:
                    p = teamA.popleft()
                    if players[p-1]:
                        players[p-1] = False
                        final[p-1] += 'A'
                        break
                aflag, bflag = False, True
            else:
                while teamB:
                    p = teamB.popleft()
                    if players[p-1]:
                        players[p-1] = False
                        final[p-1] += 'B'
                        break
                aflag, bflag = True, False

        print(''.join(final))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    function()