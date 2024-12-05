import sys
import re
import graphviz

def get_sequence():
    seq = ""
    with open(sys.argv[1], "r") as file:
        for line in file:
            if line[0] != ">":
                seq += re.sub("\n", "",line)
    return seq




def build_DeBruijn_graph(seq,k):
    G = graphviz.Digraph()
    kmers = [seq[i:i+k] for i in range(len(seq) - k)]
    for i in range(len(kmers) - 1):
        G.edge(kmers[i], kmers[i+1])
        if kmers[i][1:] == kmers[i+1][:k-1]:
            #print(kmers[i] , " -> ", kmers[i+1])
            pass
    
    G.render("debruijn", format="png", cleanup=True)
        

        

seq = get_sequence()
G = build_DeBruijn_graph(seq,10)

    