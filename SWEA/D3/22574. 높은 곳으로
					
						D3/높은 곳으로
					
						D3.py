def function():
    # T입력 받고 루프 생성, 출력은 최대 층수만
    # 루프 별로, N, P 입력 받기
    # 1부터 N까지의 정수를 모두 더하며 P와 같아지면 합에서 1을 빼고 더하기
    T = int(input())
    for _ in range(T):
        N, P = map(int, input().split())
        cnt = 0
        for n in range(1, N+1):
            cnt += n
            if cnt == P:
                cnt -= 1
        print(cnt)


if __name__ == '__main__':
    function()