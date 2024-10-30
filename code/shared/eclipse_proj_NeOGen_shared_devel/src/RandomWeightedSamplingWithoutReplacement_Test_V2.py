import random

#...............................................................................
class Node:
    # Each node in the heap has a weight, value, and total weight.
    # The total weight, self.tw, is self.w plus the weight of any children.
    __slots__ = ['w', 'v', 'tw']
    def __init__(self, w, v, tw):
        self.w, self.v, self.tw = w, v, tw

def rws_heap(items):
    # h is the heap. It's like a binary tree that lives in an array.
    # It has a Node for each pair in `items`. h[1] is the root. Each
    # other Node h[i] has a parent at h[i>>1]. Each node has up to 2
    # children, h[i<<1] and h[(i<<1)+1].  To get this nice simple
    # arithmetic, we have to leave h[0] vacant.
    h = [None]                          # leave h[0] vacant
    for w, v in items:
        h.append(Node(w, v, w))
    for i in range(len(h) - 1, 1, -1):  # total up the tws
        h[i>>1].tw += h[i].tw           # add h[i]'s total to its parent
    return h

def rws_heap_pop(h):
    gas = h[1].tw * random.random()     # start with a random amount of gas

    i = 1                     # start driving at the root
    while gas > h[i].w:       # while we have enough gas to get past node i:
        gas -= h[i].w         #   drive past node i
        i <<= 1               #   move to first child
        if gas > h[i].tw:     #   if we have enough gas:
            gas -= h[i].tw    #     drive past first child and descendants
            i += 1            #     move to second child
    w = h[i].w                # out of gas! h[i] is the selected node.
    v = h[i].v

    h[i].w = 0                # make sure this node isn't chosen again
    while i:                  # fix up total weights
        h[i].tw -= w
        i >>= 1
    return v

def random_weighted_sample_no_replacement(items, n):
    heap = rws_heap(items)              # just make a heap...
    for i in range(n):
        yield rws_heap_pop(heap)        # and pop n items off it.

def random_weighted_sample_no_replacements_inverse_weights(mapping, n):
    keys, values = zip(*mapping.items())
    total = reduce(mul, (v + 1 for v in values))
    weights = (total / (v + 1) for v in values)
    heap = rws_heap(zip(weights, keys))
    for i in xrange(n):
        yield rws_heap_pop(heap)
    
def weighted_sample(items, n):
    total = float(sum(w for w, v in items))
    i = 0
    w, v = items[0]
    while n:
        x = total * (1 - random.random() ** (1.0 / n))
        total -= x
        while x > w:
            x -= w
            i += 1
            w, v = items[i]
        w -= x
        yield v
        n -= 1
        
#...............................................................................
if __name__ == "__main__":

    items = [(10, "low"),(100, "mid"),(890, "large")]
    
    n = 100

    listResults = list(weighted_sample(items, n))
    print(str(listResults))
    
    listResults = list(random_weighted_sample_no_replacement(items, n))
    print(str(listResults))
    
    #generator = random_weighted_sample_no_replacement(items, n)
    #for i in generator:
    #    print(str(i) +",", end="")

    dictItems = {8: 0, 5: 0, 6: 1, 4: 2, 7: 3, 9: 2, 11: 1, 10: 3}
    list(random_weighted_sample_no_replacements_inverse_weights(dictItems, n))
