def function():
    T = int(input())
    basic = "abcdefghijklmnopqrstuvwxyz"
    for tc in range(1, T + 1):
        cnt = 0
        sample = input().rstrip()
        for c in range(len(sample)):
            if basic[c] == sample[c]:
                cnt += 1
            else:
                break
        print(f"#{tc} {cnt}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    function()
