
TRACE = True

if TRACE:
    def trace_cache(cache):
        for row in cache:
            for item in row:
                print('-' if item is None else item, end = ' ')
            print()
        print()

else:
    def trace_cache(*args):
        pass


def lev_imp(s1,s2):
    cache = []
    for _ in range(len(s1) + 1):
        cache.append([None] * (len(s2) + 1))
    
    for n2 in range(len(s2) + 1):
        n1 = 0
        cache[n1][n2] = n2
        trace_cache(cache)
    
    for n1 in range(len(s1) + 1):
        n2 = 0
        cache[n1][n2] = n1
        trace_cache(cache)
    
    for n1 in range(1, len(s1)+ 1):
        for n2 in range(1, len(s2) + 1):
            if(s1[n1 - 1] == s2[n2-1]):
                cache[n1][n2] = cache[n1-1][n2-1]
                trace_cache(cache)
                continue
            cache[n1][n2] = 1 + min(cache[n1-1][n2], cache[n1][n2-1], cache[n1-1][n2-1])
    trace_cache(cache)
    return cache[n1][n2]


print(lev_imp("apple", "dapple"))