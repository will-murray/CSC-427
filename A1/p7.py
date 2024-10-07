import random
import matplotlib.pyplot as plt
import sys
import copy

# accepts two intervals as input. Expects A[0] <= B[0]
def I(A, B):
    return B[0] <= A[1]
    
class Anchors:
    def __init__(self, input):
        self.L = [list(map(int,i.split(','))) for i in input.split(';')]
        self.L = sorted(self.L, key = lambda x : min(x[0], x[2]))
        self.msg = "hello"


    def overlapping(self):
        min_a,min_b = self.L[0][:2], self.L[0][2:]
        S = [anc for anc in self.L[1:] if(I(min_a, anc[:2]) or I(min_b, anc[2:]) )]

        return S
    
    def span(self, i):
        return self.L[i][1] - self.L[i][0]

    def remove_min_anchor(self):
        self.L = self.L[1:]

    def remove_overlapping_anchors(self):
        L_tup = set([tuple(l) for l in self.L]) #convert to list of tuples
        S_tup = set([tuple(s) for s in self.overlapping()])
        #print(f"{L_tup} - {S_tup} = {L_tup.difference(S_tup)}" )
        new_L =  [list(tup) for tup in L_tup.difference(S_tup)]
        new_L = sorted(new_L, key = lambda x : min(x[0], x[2]))
        self.L = new_L

def in_memo(A):
    key = tuple(tuple(a) for a in A.L)
    return key in memo.keys()
        
def remember_this(A, value):
    memo.update({tuple(tuple(a) for a in A.L) : value})

def fetch_from_memo(A):
    return memo.pop(tuple(tuple(a) for a in A.L))

# given an Anchor object, return the optimal alignment
# This function returns a list containning two elements
#
#       1) A list of anchors
#       2) the coverage of the anchors

def OPT(A):

    #check the memo
    if in_memo(A):
        return fetch_from_memo(A)

    #Base Case: Only 1 anchor
    if(len(A.L) == 1):
        return [[ A.L[0] ], A.span(0)]
    

    #find the set of anchors which overlap the leftmost anchor
    S = A.overlapping()

    #Case 2: the leftmost anchor doesn't overlap with any other anchors
    if(len(S) == 0):
        A_next = copy.deepcopy(A)
        A_next.remove_min_anchor()
        anchors, coverage = OPT(A_next)
        remember_this(A_next, [anchors, coverage])
        return [ [A.L[0]] + anchors, A.span(0) + coverage ]
        
    #Case 3: the leftmost anchor overlaps with 1 or more anchors
    A1, A2 = copy.deepcopy(A), copy.deepcopy(A)

    
    # 3.1 Compute the OPT with the leftmost anchor, excluding anchors it overlaps with
    A1.remove_overlapping_anchors()
    ancs1, cov1 = OPT(A1)

    # 3.2 Compute the OPT without the leftmost anchor
    A2.remove_min_anchor()
    ancs2, cov2 = OPT(A2)
    
    # return the option with higher coverage
    if cov1 > cov2:
        remember_this(A1, [ancs1, cov1])
        return [ancs1, cov1]

    remember_this(A2, [ancs2, cov2])
    return [ancs2, cov2]



# MAIN 

input = sys.argv[1]


A = Anchors(input)

memo = {}

ancs, coverage = OPT(A)
for a in ancs:
    print(f"({a[0]}, {a[1]}) -> ({a[2]}, {a[3]})")
print(coverage)




