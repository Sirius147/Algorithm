def function():
    # 입력 사이즈가 100이다
    # 100개의 데이터를 입력 받고, enumerate, 점수 계산 후 저장하여, 점수값으로 sort한다.
    # sort한 점수리스트에서 enumerate 값을 찾는다.
    # 해당 인덱스를 사이즈 // 10의 값으로 몫을 구하여 성적값과 매칭한다.

    T = int(input())
    sc = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

    for tc in range(1, T + 1):
        N, k = map(int,input().split())
        sectionSz = N // 10
        scores = []
        for i in range(1,N+1):
            m, f, a = map(int, input().split())
            score = m * 0.35 + f * 0.45 + a * 0.2
            scores.append([i, score])

        scores.sort(key=lambda x: x[1], reverse=True)

        for j in range(N):
            if scores[j][0] == k:
                print(f"#{tc} {sc[(j // sectionSz)]}")
                break

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    function()
