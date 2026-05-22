
def function():

    # Tc 개수는 항상 10, 루프 구성후 루프별로 #tc gap 출력하기
    # 루프별로 N, 수열 입력받기
    # N 루프별로 최댓값과 최솟값의 차이가 1보다 크면 덤프 진행, 같거나 작으면 루프 종료, 종료 후 최댓값 - 최솟값 출력
    for tc in range(1, 11):
        N = int(input())
        seq = list(map(int, input().split()))

        while N > 0:
            maxi, mini = max(seq), min(seq)
            if maxi - mini <= 1:
                break
            else:
                maxIdx, minIdx = seq.index(maxi), seq.index(mini)
                seq[maxIdx] -= 1
                seq[minIdx] += 1

            N -= 1
        print(f"#{tc} {max(seq) - min(seq)}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    function()