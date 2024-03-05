
TRACE = True

if TRACE:
    def trace_cache(cache,actions):
        for row in range(len(cache)):
            for col in range(len(cache[row])):
                item = cache[row][col]
                action = actions[row][col]
                print(f"{item} ({action})" . ljust(1),end = ' ')
            print()
        print()

else:
    def trace_cache(*args):
        pass


IGNORE = 'I'
ADD = 'A'
REMOVE = 'R'
SUBST = 'S'

def lev_imp(s1,s2):
    cache = []
    actions = []
    for _ in range(len(s1) + 1):
        cache.append(['-'] * (len(s2) + 1))
        actions.append(['-']* (len(s2) + 1))
    cache[0][0] = 0
    actions[0][0] = IGNORE
    trace_cache(cache,actions)
    
    for n2 in range(1,len(s2) + 1):
        n1 = 0
        cache[n1][n2] = n2
        actions[n1][n2] = ADD
        trace_cache(cache,actions)
    
    for n1 in range(1,len(s1) + 1):
        n2 = 0
        cache[n1][n2] = n1
        actions[n1][n2] = REMOVE
        trace_cache(cache,actions)
    
    for n1 in range(1, len(s1)+ 1):
        for n2 in range(1, len(s2) + 1):
            if(s1[n1 - 1] == s2[n2-1]):
                cache[n1][n2] = cache[n1-1][n2-1]
                actions[n1][n2] = IGNORE
                trace_cache(cache,actions)
                continue
            
            remove = cache[n1-1][n2]
            add = cache[n1][n2-1]
            subst = cache[n1 -1][n2-1]

            cache[n1][n2] = remove
            actions[n1][n2] = REMOVE

            if cache[n1][n2] > add :
                cache[n1][n2] = add
                actions[n1][n2] = ADD
            
            if cache[n1][n2] > subst:
                cache[n1][n2] = subst
                actions[n1][n2] = SUBST

            cache[n1][n2] += 1

            # cache[n1][n2] = 1 + min(cache[n1-1][n2], cache[n1][n2-1], cache[n1-1][n2-1])
    trace_cache(cache,actions)
    return cache[n1][n2]


print(lev_imp("apple", "dapple"))