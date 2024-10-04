import sys
import copy

# accepts two intervals as input. Expects A[0] <= B[0]
def I(A, B):
    return B[0] <= A[1]
    
class Anchors:
    def __init__(self, input):
         self.L = [list(map(int,i.split(','))) for i in input.split(';')]
         self.L = sorted(self.L, key = lambda x : min(x[0], x[2]))

    def overlapping(self):
        min_a,min_b = self.L[0][:2], self.L[0][2:]
        S = [anc for anc in self.L[1:] if(I(min_a, anc[:2]) or I(min_b, anc[2:]) )]

        return S
    
    def span(self, i):
        return self.L[i][1] - self.L[i][0]

    def remove_min_anchor(self):
        self.L = self.L[1:]

#given an Anchor object, return the optimal alignment
#This function returns a list containning two elements
#
#       1) A list of anchors
#       2) the coverage of the anchors
#

def OPT(A):

    #empty list containing the anchors to choose
    

    #Base Case: Only 1 anchor
    if(len(A.L) == 1):
        print(f"BASE CASE, returning = [{A.L[0]}, {A.span(0)}] ")
        return [[ A.L[0] ], A.span(0)]

    #find the set of anchors which overlap the leftmost anchor
    S = A.overlapping()

    A_next = copy.deepcopy(A)

    #Case 2: the leftmost anchor doesn't overlap with any other anchors
    if(len(S) == 0):
        A_next.remove_min_anchor()
        anchors, coverage = OPT(A_next)
        print(f"anchors = {anchors}, coverage = {coverage}")
        print(f"A.L[0] = {A.L[0]}" )
        return [ [A.L[0]] + anchors, A.span(0) + coverage ]
        



input = sys.argv[1]

A = Anchors(input)

print(OPT(A))




