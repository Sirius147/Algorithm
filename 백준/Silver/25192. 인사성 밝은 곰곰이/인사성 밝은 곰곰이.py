import sys
input = sys.stdin.readlines

strs = input()
strs = strs[2:]

sett = set(); cnt = 0
for string in strs:
    if string == 'ENTER\n':
        cnt += len(sett)
        sett.clear()
        continue
    sett.add(string)
cnt += len(sett)  
print(cnt)