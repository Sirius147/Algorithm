import math
def function():
    # T 입력 받고, #tc로 출력 구분, 점수의 총합 출력
    # 루프 별로 N입력 받기
    # N 회 루프 별로 점수 합산, 루프 별로 x,y좌표 입력 받고 제곱해 더한 후 스퀘어 루트로 반지름 구하기
    # 11 - 해당 반지름 값 / 20 을 int 처리하여 점수 구하기 이 때 반지름 값이 0인경우 즉 점수가 11점인 경우 10점으로 변환
    T = int(input())
    for tc in range(1, T + 1):
        N = int(input())
        cnt = 0
        for _ in range(N):
            x, y = map(int, input().split())
            r = math.sqrt((x ** 2 + y ** 2))
            tmp = 11 - (r / 20)
            p = int(tmp)
            if p == 11:
                p = 10
            if p <= 0:
                continue
            cnt += p
        print(f"#{tc} {cnt}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    function()