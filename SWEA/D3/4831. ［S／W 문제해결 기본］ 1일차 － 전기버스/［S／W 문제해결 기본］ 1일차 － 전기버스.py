def function():
    # T를 입력받아 루프 형성, tc로 출력
    # K, N, M 순으로 입력받기
    # 길이 N+1의 리스트 생성
    # M개 길이의 입력을 N+1리스트의 인덱스로 활용해 상태관리하기
    # 인덱스 0에서 시작 K 거리 ex 3,2,1 인덱스에 목적지 있는 지 확인, 목적지 있으면 종료
    # 없으면 정류장 있는 지 확인, 정류장인덱스 중 가장 먼 인덱스가 다음 위치, cnt += 1, 정류장 없으면 cnt = 0 종료
    T = int(input())
    for tc in range(1, T + 1):
        K, N, M = map(int, input().split())
        road = [0 for _ in range(N + 1)]
        for i in map(int, input().split()):
            road[i] = 1
        idx, cnt = 0, 0

        while idx + K < N:
            station = False
            for j in range(K, 0, -1):
                if road[idx + j]:
                    idx = idx + j
                    cnt += 1
                    station = True
                    break
            if station:
                continue
            else:
                cnt = 0
                break

        print(f"#{tc} {cnt}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    function()