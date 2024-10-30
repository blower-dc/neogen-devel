import random
import functools
from operator import mul

class Node:
    __slots__ = ['w', 'v', 'tw']
    def __init__(self, w, v, tw):
        self.w, self.v, self.tw = w, v, tw

def rws_heap(items):
    h = [None]
    for w, v in items:
        h.append(Node(w, v, w))
    for i in range(len(h) - 1, 1, -1):
        h[i>>1].tw += h[i].tw
    return h

def rws_heap_pop(h):
    gas, i = h[1].tw * random.random(), 1
    while gas > h[i].w:
        gas -= h[i].w
        i <<= 1
        if gas > h[i].tw:
            gas -= h[i].tw
            i += 1
    w, v = h[i].w, h[i].v
    h[i].w = 0
    while i:
        h[i].tw -= w
        i >>= 1
    return v

def random_weighted_sample_no_replacement(items, n):
    heap = rws_heap(items)
    for i in range(n):
        yield rws_heap_pop(heap)

def random_weighted_sample_no_replacements_weighted_towards_lower_values(mapping, n):
    #Lower values are wighted highest
    keys, values = zip(*mapping.items())
    total = functools.reduce(mul, (v + 1 for v in values))
    weights = (total / (v + 1) for v in values)
    heap = rws_heap(zip(weights, keys))
    for i in range(n):
        yield rws_heap_pop(heap)
        
def random_weighted_sample_no_replacements_weighted_towards_higher_values(mapping, n):
    #Higher values are wighted highest
    keys, values = zip(*mapping.items())
    #total = functools.reduce(mul, (v + 1 for v in values))
    weights = (v for v in values)
    heap = rws_heap(zip(weights, keys))
    for i in range(n):
        yield rws_heap_pop(heap)

#...............................................................................
if __name__ == "__main__":

    n = 3

    
    dictItems = {12: 0, 13: 0, 8: 0, 5: 0, 6: 1, 4: 2, 7: 3, 9: 2, 11: 1, 10: 3}

    dictItems = {1: 0, 2: 0, 3: 0, 4: 1, 5: 1, 6: 2, 7: 2, 9: 2, 10: 3, 11: 3, 12: 3, 14: 4, 15: 4, 15: 5, 16: 5, 17:6, 18: 6, 19: 6}
    
    listResults = list(random_weighted_sample_no_replacements_weighted_towards_lower_values(dictItems, n))
    print('Weighted_towards_lower_values:' + str(listResults) + ' Score=' + str(sum(listResults)))
    
    listResults = list(random_weighted_sample_no_replacements_weighted_towards_higher_values(dictItems, n))
    print('Weighted_towards_higher_values:' + str(listResults) + ' Score=' + str(sum(listResults)))
    #print(str(sorted(listResults)))
