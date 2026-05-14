def function():
    T = int(input())
    for tc in range(1, T+1):
        N, M = map(int, input().split())
        A = list(map(int, input().split()))
        A.sort()
        B = list(map(int, input().split()))
        cnt = 0

        def biSearch(l, r, target):

            ls, rs = False, False
            if A[(l+r)//2] == target:
                return (l+r)//2, True

            while l < r:
                m = (l + r) // 2
                if A[m] < target:
                    if ls:
                        return 0, False
                    l = m + 1
                    ls = True
                    rs = False
                elif A[m] == target:
                    return m, True
                else:
                    if rs:
                        return 0, False
                    r = m - 1
                    rs = True
                    ls = False

            return l, True

        for n in B:
            idx, check = biSearch(0, len(A) - 1, n)
            if A[idx] == n and check:
                cnt += 1
        print(f"#{tc} {cnt}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    function()
