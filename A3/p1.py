import sys
import re

fasta_fname = sys.argv[1]

def get_reads():
    reads = []
    with open(fasta_fname, "r") as file:
        for line in file:
            if line[0] in ['A', 'C', 'T', 'G']:
                reads.append(re.sub("\n","",line))
    return reads

def max_prefix_suffix_match(str1, str2):
    for l in reversed(range(len(str1))):
        k = len(str1) - l
        if(str1[:l] == str2[k:]):
            if len(str1[:l]) >= 10:
                print(f"{str1[:l]}{str1[l:].lower()} : {str2[:k].lower()}{str2[k:]}")
            return len(str1[:l])
        
    return 0

def find_adjacencies(nodes):
    for i, node_i in enumerate(nodes):
        for j,node_j in enumerate(nodes):
            w = max_prefix_suffix_match(node_i,node_j)
            if w > 10 and i != j:
                print(f"{i} <-> {j} : {w}")


    
find_adjacencies(get_reads())
