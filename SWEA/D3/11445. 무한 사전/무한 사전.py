def function():
    # T 입력 받고 루프 생성, # tc로 출력 관리
    # 첫줄에 단어 P 입력, 두번 째 줄에 단어 Q입력 받음
    # p는 먼저오는 단어이므로 p의 즉시 다음 단어인 p + a와 q가 같으면 N 다르면 Y 출력
    T = int(input())
    for tc in range(1, T+1):
        P = input().rstrip()
        Q = input().rstrip()
        comp = P + "a"
        if Q != comp:
            print(f"#{tc} Y")
        else:
            print(f"#{tc} N")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    function()
