parent_lst = [i for i in range(101)]

def solution(n, costs):
    answer = 0

    def find_root(x):
        global parent_lst
        if parent_lst[x] == x:
            return x
        parent_lst[x] = find_root(parent_lst[x])
        return parent_lst[x]
    
    def union_root(a, b):
        global parent_lst
        a = find_root(a)
        b = find_root(b)
        
        if a < b:
            parent_lst[b] = a
        else:
            parent_lst[a] = b
    
    costs.sort(key=lambda x:x[2])
    
    for a, b, p in costs:
        if find_root(a) == find_root(b):
            continue
        else:
            union_root(a, b)
            answer += p
        if sum(parent_lst) == 0:
            break

    return answer