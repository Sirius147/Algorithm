def function():

    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        all = (10 ** N) - (10 ** (N-1))
        cnt = 1
        avail = 10
        while N:
            if avail == 10:
                cnt *= 9
                avail -= 1
            else:
                cnt *= avail
                avail -= 1

            N -= 1
        print(f"#{tc} {cnt/all:.5f}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    function()
