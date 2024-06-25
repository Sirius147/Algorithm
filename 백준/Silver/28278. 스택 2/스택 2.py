import sys
class Stack():
    def __init__(self):
        self.__list = []
        self.__len = 0
    def insert(self,x:int):
        self.__list.append(x)
        self.__len += 1
    def pop(self):
        if self.isEmpty(): return -1
        self.__len -= 1
        return self.__list.pop(-1)
    def size(self):
        return self.__len
    def isEmpty(self):
        if self.__len: return 0
        return 1
    def top(self):
        if self.isEmpty(): return -1
        return self.__list[-1]

input = sys.stdin.readline
n = int(input())
stack = Stack()
while n > 0:
    cmd = list(map(int,input().split()))
    if cmd[0] == 1:
        stack.insert(cmd[1])
    elif cmd[0] == 2:
        sys.stdout.write(str(stack.pop())+'\n')
    elif cmd[0] == 3:
        sys.stdout.write(str(stack.size())+'\n')
    elif cmd[0] == 4:
        sys.stdout.write(str(stack.isEmpty())+'\n')
    else: sys.stdout.write(str(stack.top())+'\n')
    n-=1