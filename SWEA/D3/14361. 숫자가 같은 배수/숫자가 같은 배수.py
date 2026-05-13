def function():
    # T 입력 받고 루프생성, tc로 출력 번호 관리
    # 루프마다 자연수 N (1 ~ 10 ** 6) 문자열로 입력받기
    # 해당 숫자 문자열의 자릿수 기준 자릿수가 하나 더 늘어나기 전까지 정수화해서 곱하고 다시 문자열로 만들어 활용하기
    # 곱하여 나온 수 요소하나씩 원래 문자열에 있는 지 확인하기 모두 있으면 possible 출력 하나라도 없으면 impossible 출력
    T = int(input())
    for tc in range(1, T + 1):
        N = input().rstrip()
        n = sorted(N)
        digit = len(N)
        i = 2
        tmp = int(N) * i
        flag = False

        while len(str(tmp)) == digit:
            if sorted(str(tmp)) == n:
                flag = True
                print(f"#{tc} possible")
                break
            else:
                i += 1
                tmp = int(N) * i
        if not flag:
            print(f"#{tc} impossible")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    function()
