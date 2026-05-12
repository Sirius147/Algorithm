import math



def isP(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def function():
    # T 입력 받고 루프 생성, tc 별로 출력
    # a,b입력 받기
    # a 초과 b 미만인 정수들 대상으로 소수여부 검사
    # shortcut을 위해 검사 대상을 2부터 루트 검사대상(정수화해야함) 포함하여 검사
    # 소수 맞을 경우 리스트에 담고 최종에 합을 출력하기
    T = int(input())
    for tc in range(1, T + 1):
        plist = []
        a, b = map(int, input().split())
        for i in range(a + 1, b):
            if isP(i):
                plist.append(i)
        print(f"#{tc} {sum(plist)}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    function()
