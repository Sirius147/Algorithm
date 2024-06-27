from collections import deque
import sys
input = sys.stdin.readlines
inputs = input()
inputs.pop(0)

deq = deque()

for com in inputs:
    if com[0] == '1':
        deq.appendleft(int(com.split()[1]))

    elif com[0] == '2':
        deq.append(int(com.split()[1]))

    elif com[0] == '3':
        if len(deq):
            print(deq.popleft())
    
        else: print(-1)
    elif com[0] == '4':
        if len(deq):
            print(deq.pop())
          
        else: print(-1)
    elif com[0] == '5':
        print(len(deq))

    elif com[0] == '6':
        if len(deq):
            print(0)
    
        else: print(1)
    elif com[0] == '7':
        if len(deq): 
            print(deq[0])
    
        else: print(-1)
    else:
        if len(deq): 
            print(deq[-1])
    
        else: print(-1) 


    

    