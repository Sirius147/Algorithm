def function():
    # T 입력 받고 루프 구성, #tc로 출력 구분, yes/no 출력
    # 루프 별로 그리드 사이즈 N 입력 받기
    # 그리드전체에 #의개수 count 하고 해당 숫자가 제곱수가 아니면 no, 제곱 수면 한변의 길이 구하기
    # 그리드 전체를 돌면서 #을 찾기, #의 위치에서 한변길이의 이중루프 구성하여 정사각형 성립여부 확인, 하나라도 없으면 no 통과하면 true
    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        grid = [input().rstrip() for _ in range(N)]
        cnt = 0
        for item in grid:
            cnt += item.count('#')
        con1 = False
        n = 1
        for i in range(1, N+1):
            if cnt == (i ** 2):
                con1 = True
                n = i

        if not con1:
            print(f"#{tc} no")
            continue

        for row in range(N - n + 1):
            for col in range(N - n + 1):
                out = False
                cnt = n
                if grid[row][col] == '#':
                    flag = True
                    for i in range(n):
                        if grid[row + i][col:col+n].count('#') != cnt:
                            flag = False
                            break
                    if flag:
                        print(f"#{tc} yes")
                    if not flag:
                        print(f"#{tc} no")
                    out = True
                    break
            if out:
                break
        

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    function()