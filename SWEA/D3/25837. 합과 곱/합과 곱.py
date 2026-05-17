def function():
    # T 값 입력 받고 루프 생성, tc별로 출력 x 케이스별로 Yes/No
    # N, M 순서대로 입력받기
    # N의 가능한 범위는 1 ~ (N+M)//2
    # 해당 범위 숫자로 이분탐색, 값이 존재하면 Yes 없으면 No 출력하기
    # 보수 값과의 곱셈으로 이분탐색 범위 조정하기

    T = int(input())
    for _ in range(T):
        S, P = map(int, input().split())
        l, r = 1, S // 2

        def biSearch(l, r):

            while l < r:
                m = (l + r) // 2
                n = S - m
                p = m * n
                if p < P:
                    l = m + 1
                else:
                    r = m

            return l

        n = biSearch(l, r)
        if (S - n) * n == P:
            print("Yes")
        else:
            print("No")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    function()