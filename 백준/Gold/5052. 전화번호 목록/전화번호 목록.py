def insert(trie, word):
    cur_node = trie
    for char in word:
        if '*' in cur_node:
            return False

        if char not in cur_node:
            cur_node[char] = {}
        cur_node = cur_node[char]
    
    if cur_node:
        return False
    
    cur_node['*'] = True
    return True

T = int(input())

for _ in range(T):
    N = int(input())
    trie = {}
    ok = True
    for _ in range(N):
        s = input()
        if not ok:
            continue
        if not insert(trie, s):
            ok = False
    if ok:
        print("YES")
    else:
        print("NO")