#!/usr/bin/env python3

import functools
import pprint


# pp = pprint.PrettyPrinter(indent = 4)


def trace_cache(cache):
    for row in cache:
        for item in row:
            print('-' if item is None else item, end = ' ')
        print()
    print()

# @functools.lru_cache(maxsize = None)
def lev_imp(s1,s2,n1,n2,cache):

    # using the cache
    if cache[n1][n2] is not None :
        trace_cache(cache)
        return cache[n1][n2]
    

    if(n1 == 0):
        cache[n1][n2] = n2
        trace_cache(cache)
        return cache[n1][n2]
    
    if(n2 == 0):
        cache[n1][n2] = n1
        trace_cache(cache)
        return cache[n1][n2]
    

    if(s1[n1-1] == s2[n2 - 1]):
        cache[n1][n2] = lev_imp(s1,s2, n1-1, n2-1,cache) #ignore
        trace_cache(cache)
        return cache[n1][n2]
    
    # 1 + to account for the the last character that we are adding,replacing or removing.
    cache[n1][n2] = 1 + min(lev_imp(s1,s2,n1-1,n2,cache), #remove
              lev_imp(s1,s2, n1, n2-1,cache), #add
              lev_imp(s1,s2, n1-1, n2-1,cache)) #replace
    trace_cache(cache)
    return cache[n1][n2]



def lev(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    cache = []

    for _ in range(n1 + 1): 
        cache.append([None]* (n2 + 1))

    return lev_imp(s1,s2,n1,n2,cache)

print(lev("tea","ear"))
# print(lev("apple", "dapple"))

# print(lev("add","daddy"))
# print(lev("apple", "de2wdn"))