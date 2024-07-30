import sys
input = sys.stdin.readline  

track = []

def merge(L:list,s_idx:int,m_idx:int,e_idx:int):
    global track
    temp = []; idx = 0
    s = s_idx; m = m_idx + 1; e = e_idx
    while s <= m_idx and m <= e_idx:
        if L[s] <= L[m]:
            temp.append(L[s]); idx += 1
            track.append(L[s]); s += 1
        else:
            temp.append(L[m]); idx += 1
            track.append(L[m]); m += 1
    while m <= e_idx:
        temp.append(L[m]); idx += 1
        track.append(L[m]); m += 1
    while s <= m_idx:
        temp.append(L[s]); idx += 1
        track.append(L[s]); s += 1
    L[s_idx:e_idx+1] = temp
            

def merge_sort(L:list,s_idx:int,e_idx:int):
    
    if(s_idx < e_idx):
        m_idx = (s_idx + e_idx)//2
        merge_sort(L,s_idx,m_idx)
        merge_sort(L,m_idx+1,e_idx)
        merge(L,s_idx,m_idx,e_idx)
    

length, turn = map(int, input().split())
sample = list(map(int, input().split()))
merge_sort(sample,0,len(sample)-1)
if turn > len(track):
    print(-1)
    exit(0)
print(track[turn-1]) 