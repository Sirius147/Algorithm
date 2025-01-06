import sys
input = sys.stdin.readline


def solve(arg:int):
    p = [1,1,1,2,2] + [0] * 95
    for i in range(5,arg):
        p[i] = p[i-1] + p[i-5]
    
    print(p[arg-1])


if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        arg = int(input())
        solve(arg)
        

