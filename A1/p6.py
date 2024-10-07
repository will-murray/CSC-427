import sys
import re


#returns the reverse complement of a string s
def rc(s):
    d = {"A":"T", "T":"A", "C":"G", "G":"C" , "N":"N"}
    
    rc_s = ''.join([d[chr] for chr in s]) #complement
    rc_s = rc_s[::-1]   #reverse
        
    return(rc_s)

def build_kmer_list(str,k):
    return [str[i:i+k] for i in range(len(str) - k + 1 )] #nasty list comprehension

#returns the lexicographically smallest k-mer given a string str and an integer k
def min_k_mer(str,k):
    kmers = build_kmer_list(str,k)
    return sorted(kmers)[0]

def canon_min_k_mer(str,k):
    k_mers = build_kmer_list(str,k) + build_kmer_list(rc(str), k)
    return sorted(k_mers)[0]


def ORCOM_min_k_mer(str,k):
    k_mers = build_kmer_list(str,k) + build_kmer_list(rc(str), k)
    #consider all k-mers which dont contain such a pattern
    k_mers = [mer for mer in k_mers if re.search(r'(.)\1{2}', mer) is None]

    if len(k_mers) > 0:
        return sorted(k_mers)[0]

# sys.argv[1] contains the path to the temporary file created by process substitution
input_file = sys.argv[1]
k = int(sys.argv[2])

# Open and read the file like a normal file
with open(input_file, 'r') as f:
    data = f.readlines()
    
idx = 0 
N = len(data)
#parse 4 lines at a time
while idx < N:
    name = data[idx].split(" ")[0] #extract the read name (first token before the whitespace char)
    seq = re.sub("\n", "", data[idx + 1]) #extract the sequence and remove the newline character

    print(f"{name}\t{min_k_mer(seq,k)}\t{canon_min_k_mer(seq,k)}\t{ORCOM_min_k_mer(seq,k)}")
    idx +=4

#s = "TNGCNGAGAGTTCTACAAGTTTTAGCGTACTACTGAACAATAATGTCCTTATTTTTTATATCTCGCGCATATTTGGAGGCCATATCGTGCCACCAACTTTA"
#print(min_k_mer(s, 16) == "AACAATAATGTCCTTA")
#print(canon_min_k_mer(s, 16) == "AAAAAATAAGGACATT")
#print(ORCOM_min_k_mer(s, 16) == "AACAATAATGTCCTTA")
