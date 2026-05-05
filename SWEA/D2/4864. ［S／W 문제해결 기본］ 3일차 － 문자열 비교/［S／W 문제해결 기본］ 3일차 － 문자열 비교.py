def function():
    T = int(input())
    for tc in range(1, T + 1):
        str1 = input().rstrip()
        str2 = input().rstrip()
        if str2.count(str1):
            print(f"#{tc} 1")
        else:
            print(f"#{tc} 0")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    function()