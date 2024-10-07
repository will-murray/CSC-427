import sys
import re


assert(len(sys.argv) == 4)
tokens = re.findall(r'\d+[a-zA-Z]+', sys.argv[3])
s1, s2 = sys.argv[1], sys.argv[2]

seq1 = ""
mid = ""
seq2 = ""


for toke in tokens:
    action = toke[len(toke) - 1] #type of difference 
    N = int(toke[0:len(toke) - 1]) #num differences

    #match/ mismatch
    if action == "M": 
        mid_string = ""

        for a,b in zip(s1[0:N], s2[0:N]):
            if a == b:
                mid_string += "|"
            else:
                mid_string += "*"

        #update the output strings
        mid += mid_string
        seq1 += s1[0:N]
        seq2 += s2[0:N]

        #remove the characters that have just been processed from the strings
        s1 = s1[N:]
        s2 = s2[N:]

    elif action == "I": #insertion
        mid += "*"*N
        seq1 += s1[0:N]
        seq2 += "-"*N 
        s1 = s1[N:]

    elif action == "D":
        mid += "*"*N
        seq2 += s2[0:N]
        seq1 += "-"*N 
        s2 = s2[N:]

    elif action == "X":
        mid += "*"*N
        seq1 += s1[0:N]
        seq2 += s2[0:N]


    elif action == "=":
        mid += "="*N
        seq1 += s1[0:N]
        seq2 += s2[0:N]


    

    seq1 += " "
    seq2 += " "
    mid += " "

             
        

print(seq1)
print(mid)
print(seq2)
    





