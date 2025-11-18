from collections import defaultdict
from bisect import bisect_left
def solution(info, query):

    db = defaultdict(list)
    answer = []
    
    for i in info:
        s = i.split()
        keys = s[:-1]
        val = int(s[-1])
        k = ""
        for a in [keys[0],"-"]:
            for b in [keys[1], "-"]:
                for c in [keys[2], "-"]:
                    for d in [keys[3], "-"]:
                        k =  a + b + c + d
                        db[k].append(val)
                        
    for key in db.keys():
        
        db[key].sort()
        
    for q in query:
        q = q.replace("and","",3)
        s = q.split()
        keys = s[:-1]
        val = int(s[-1])
        target = db["".join(keys)]
        targetLen = len(target)
        nums = targetLen - bisect_left(db["".join(keys)],val)
        answer.append(nums)
        
    return answer