import sys
import re
import math

def rc(s):
    d = {"A": "T", "T": "A", "C": "G", "G": "C", "N": "N"}
    
    rc_s = ''.join([d[chr] for chr in s])  # complement
    rc_s = rc_s[::-1]  # reverse
    return rc_s

# Get the sequence associated with the given sequence name
def extract_sequence(name, ref):
    with open(ref, 'r') as file:
        data = file.read()
    data = [d for d in data.split(">") if d.startswith(name)][0]  # extract the chromosome
    data = re.sub(name, '', data)  # remove the name
    data = re.sub('\n', '', data)  # remove newline characters
    return data

# Samples a fragment once every t/d steps
def generate_fragments(seq, t, d,l):
    fragments = []
    positions = []
    for i in range(len(seq) - t):
        if i % math.floor(t / d) == 0:
            fragments.append(seq[i:i + t])
            positions.append((i +1, i+1+l))

    return fragments, positions

# Given a fragment return the first and second mate
def sequence_fragment(frag, l):
    first = frag[:l]
    second = rc(frag[len(frag) - l:])

    return first, second

# Create a valid SAM file
def write_sam_file(fragments, positions, name, l):
    with open(f"{name}.sam", "w") as sam_file:
        # Write SAM header
        sam_file.write("@HD\tVN:1.6\tSO:coordinate\n")
        sam_file.write(f"@SQ\tSN:{name}\tLN:{len(fragments[0])}\n")

        # Write each fragment's paired reads
        for i, (frag, pos) in enumerate(zip(fragments, positions)):
            first_read_name = f"read_{name}_{pos[0]}"
            second_read_name = first_read_name  # Same name for both mates

            # First mate
            sam_file.write(f"{first_read_name}\t99\t{name}\t{pos[0]}\t0\t{l}M\t=\t0\t0\t{frag[:l]}\t*\n")

            # Second mate
            sam_file.write(f"{second_read_name}\t147\t{name}\t{pos[1]}\t0\t{l}M\t=\t0\t0\t{rc(frag[len(frag) - l:])}\t*\n")

if __name__ == "__main__":
    ref, name, l, t, d = sys.argv[1:]
    l, t, d = int(l), int(t), int(d)

    print(f"step size = {math.floor(t/d)}")

    sequence = extract_sequence(name, ref)
    fragments, positions = generate_fragments(sequence, t, d, l)

    # Write the SAM file
    write_sam_file(fragments, positions, name, l)
