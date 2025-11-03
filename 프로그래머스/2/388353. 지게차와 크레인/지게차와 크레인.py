def solution(storage, requests):
    
    def chain(r,c):
        
        check = False
        
        for dx, dy in [(-1,0), (1, 0), (0, -1), (0, 1)]:
            rr,cc = r + dx, c + dy
            if storage[rr][cc] == "0":
                storage[r][c] = "0"
                check = True
                break
        if check:
            for dx, dy in [(-1,0), (1, 0), (0, -1), (0, 1)]:
                rr,cc = r + dx, c + dy
                if storage[rr][cc] == "1":
                    storage[rr][cc] = "0"
                    chain(rr,cc)
                    
                    
    storage = [list("0"+ s+ "0") for s in storage]

    storage.insert(0, list("0" * (len(storage[0]))))
    storage.append(list("0" * (len(storage[0]))))
    
    row = len(storage)
    col = len(storage[0])
    
    for req in requests:
        if len(req) == 1:
            chains = []
            for r in range(1,row-1):
                for c in range(1,col-1):
                    if storage[r][c] == req[0]:
                        for dx, dy in [(-1,0), (1, 0), (0, -1), (0, 1)]:
                            rr, cc = r+dx, c+dy
                            if storage[rr][cc] == "0":
                                chains.append((r,c))
                                break
                                
            for c in chains:
                storage[c[0]][c[1]] = "0"
                chain(*c)
        else:
            for r in range(1,row-1):
                for c in range(1,col-1):
                    if storage[r][c] == req[0]:
                        storage[r][c] = "1"
                        chain(r,c)
                                       
    
    answer = 0
    for r in range(1,row-1):
        for c in range(1,col-1):
            if 'A' <= storage[r][c] <= 'Z':
                answer += 1
    
    return answer