def function():
    # T 입력 받고 루프생성, tc로 출력 번호 관리
    # 자연수 N 입력 받고 리스트로 변환하며, 각 숫자를 노드로하는 상태리스트, 노드 갯수 카운트 변수 생성
    # 첫 자리는 0이 안되게 노드 상태 조정, 노드 개수가 자릿수가 되면 해당 탐색 검증 int 연산으로 2배수 이상임을 검증
    # 검증 된 자릿수가 있다면 결과 리스트에 True 저장

    T = int(input())
    for tc in range(1, T + 1):
        N = list(input().rstrip())
        visited = [False for _ in range(len(N))]
        ans = [False]

        def dfs(tmp):
            if len(tmp) == len(N):
                itmp, iN = int(''.join(tmp)), int(''.join(N))
                if itmp % iN == 0 and itmp // iN > 1:
                    ans[0] = True

            for i in range(len(N)):
                if not visited[i]:
                    visited[i] = True
                    tmp.append(N[i])
                    dfs(tmp)
                    visited[i] = False
                    tmp.pop()

        dfs([])
        if ans[0]:
            print(f"#{tc} possible")
        else:
            print(f"#{tc} impossible")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    function()