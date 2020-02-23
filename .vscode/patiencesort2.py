from collections import namedtuple
from functools import total_ordering
from bisect import bisect_left
from bisect import bisect_right
 
@total_ordering
class Node:
    def __init__(self, x,y, back=None):
        self.x = x
        self.y = y
        self.back = back
    def __iter__(self):
        while self is not None:
            yield (self.x,self.y)
            self = self.back
    def __lt__(self, other):
        return self.x < other.x and self.y < other.y
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
 
def lis(d):
    """Return one of the L.I.S. of list d using patience sorting."""
    if not d:
        return []
    pileTops = []
    for (x,y) in d:
        j = bisect_left(pileTops, Node(x,y, None))
        new_node = Node(x,y, pileTops[j-1] if j > 0 else None)
        if j == len(pileTops):
            pileTops.append(new_node)
        else:
            pileTops[j] = new_node
 
    return list(pileTops[-1])[::-1]
 


d = [(2,4),(6,1), (5,7)]
print(lis(d))