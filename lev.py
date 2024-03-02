#!/usr/bin/env python3

import functools

@functools.lru_cache(maxsize = None)
def lev_imp(s1,s2,n1,n2):
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)
    if(s1[-1]==s2[-1]):
        return lev_imp(s1[:-1],s2[:-1])
    
    # 1 + to account for the the last character that we are adding,replacing or removing.
    return 1 + min(lev_imp(s1[:-1],s2), #remove
              lev_imp(s1,s2[:-1]), #add
              lev_imp(s1[:-1],s2[:-1])) #replace


def lev(s1, s2):
    return lev_imp(s1,s2,len(s1),lev(s2))

print(lev("apple","apple"))
print(lev("apple", "dapple"))