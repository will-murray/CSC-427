import sys
import re
import graphviz


assert(len(sys.argv) == 2)
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
                return len(str1[:l])
        
    return 0

def build_dot_graph(nodes):
    G = graphviz.Digraph()

    for i, node_i in enumerate(nodes):
        for j,node_j in enumerate(nodes):
            w = max_prefix_suffix_match(node_i,node_j)
            if w > 10 and i!=j:
                G.edge(node_i,node_j,label=str(w))

    G.render("overlap", format="png", cleanup=True)
    
build_dot_graph(get_reads())
