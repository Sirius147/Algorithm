import sys
input = sys.stdin.readline

lEngth = int(input())
seq = list(map(int,input().split()))

opsBucket = list(map(int,input().split()))
ops = ""; opsDict = {0:'+', 1:'-', 2:'*', 3:'/'}
for i in range(len(opsBucket)):
    ops += opsDict[i]*opsBucket[i]
ops = list(ops)

opsStates = [False for _ in range(len(ops))]

results = set()

def backtracking(level:int,preVal:int):
    if level == len(seq):
        results.add(preVal)
        return
    def operation(op,oper1,oper2)->int:
        if op == '+':
            return oper1 + oper2
        elif op == '-':
            return oper1 - oper2
        elif op == '*':
            return oper1 * oper2
        else:
            if oper1 < 0 and oper2 > 0:
                oper1 *= -1
                tmp = oper1 // oper2
                return -1 * tmp
            return oper1 // oper2
        

    for i in range(len(ops)):
        if opsStates[i] == False:
            newVal = operation(ops[i],preVal,seq[level])
            opsStates[i] = True
            backtracking(level+1,newVal)
            opsStates[i] = False


backtracking(1,seq[0])
print(max(results),min(results),sep = '\n')