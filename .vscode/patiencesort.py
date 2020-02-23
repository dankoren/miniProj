import bisect
from collections import defaultdict

# We want a maximum function which accepts a default value
from functools import partial, reduce
maximum = partial(reduce, max)

def patience_sort(xs):
    print("aaa")
    '''Patience sort an iterable, xs.
    
    This function generates a series of pairs (x, pile), where "pile"
    is the 0-based index of the pile "x" should be placed on top of.
    Elements of "xs" must be less-than comparable.
    '''
    pile_tops = list()
    for x in xs:
        pile = bisect.bisect_left(pile_tops, x)
        if pile == len(pile_tops):
            pile_tops.append(x)
        else:
            pile_tops[pile] = x
        yield x, pile

def longest_increasing_subseq_length(xs):
    '''Return the length of the longest increasing subsequence of xs.
    
    >>> longest_increasing_subseq_length(range(3))
    3
    >>> longest_increasing_subseq_length([3, 1, 2, 0])
    2
    '''
    return 1 + maximum((pile for x, pile in patience_sort(xs)), -1)

def longest_increasing_subsequence(xs):
    '''Return a longest increasing subsequence of xs.
    
    (Note that there may be more than one such subsequence.)
    >>> longest_increasing_subsequence(range(3))
    [0, 1, 2]
    >>> longest_increasing_subsequence([3, 1, 2, 0])
    [1, 2]
    '''
    # Patience sort xs, stacking (x, prev_ix) pairs on the piles.
    # Prev_ix indexes the element at the top of the previous pile,
    # which has a lower x value than the current x value.
    piles = [[]] # Create a dummy pile 0
    for x, p in patience_sort(xs):
        if p + 1 == len(piles):
            piles.append([])
        # backlink to the top of the previous pile
        piles[p + 1].append((x, len(piles[p]) - 1)) 
    # Backtrack to find a longest increasing subsequence
    npiles = len(piles) - 1
    prev = 0
    lis = list()
    for pile in range(npiles, 0, -1):
        x, prev = piles[pile][prev]
        lis.append(x)
    lis.reverse()
    return lis


def foo():
    print("bbb")


print(list([(1,2),(4)]))
foo()
patience_sort([1,2,3])
