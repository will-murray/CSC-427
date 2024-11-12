import sys

def read_fasta(fasta_file):
    """Reads a FASTA file and returns the sequence as a dictionary {chromosome: sequence}."""
    sequences = {}
    with open(fasta_file, "r") as f:
        chrom = None
        seq_lines = []
        for line in f:
            if line.startswith(">"):
                if chrom:
                    sequences[chrom] = "".join(seq_lines).upper()
                chrom = line[1:].strip()
                seq_lines = []
            else:
                seq_lines.append(line.strip())
        if chrom:
            sequences[chrom] = "".join(seq_lines).upper()
    return sequences

def preprocess_data(sam_file):
    # Load the reference genome
    

    # Dictionary to store coverage information: {position: {allele: count}}
    coverage = {}

    # Process each alignment line in the SAM file
    with open(sam_file, "r") as f:
        for line in f:
            if not line.startswith("@"):
                fields = line.split()
                chrom = fields[2]
                ref_start = int(fields[3]) - 1  # Convert to 0-based index
                cigar = fields[5]
                read_seq = fields[9]

                ref_pos = ref_start
                read_pos = 0
                i = 0
                while i < len(cigar):
                    j = i
                    while cigar[j].isdigit():
                        j += 1
                    size = int(cigar[i:j])
                    op = cigar[j]
                    i = j + 1

                    if op == 'M':  # Match/mismatch
                        for k in range(size):
                            ref_base = ref_sequences[chrom][ref_pos]
                            read_base = read_seq[read_pos]
                            
                            # Initialize the nested dictionary if it doesn't exist
                            if ref_pos not in coverage:
                                coverage[ref_pos] = {}
                            if read_base not in coverage[ref_pos]:
                                coverage[ref_pos][read_base] = 0
                            
                            # Increment the count for this allele
                            coverage[ref_pos][read_base] += 1
                            ref_pos += 1
                            read_pos += 1
                    elif op == 'I':  # Insertion in the read
                        read_pos += size
                    elif op == 'D':  # Deletion in the reference
                        ref_pos += size
                    elif op == 'S':  # Soft clipping (ignored in reference)
                        read_pos += size
                    elif op == 'N':  # Skipped region in reference
                        ref_pos += size

    return coverage


# Example usage:
# coverage_data = preprocess_data("chr22.fa", "test.sam")
# This `coverage_data` dictionary will have counts of each allele at each position.

ref_fname = sys.argv[1]
align_fname = sys.argv[2]

ref_sequences = read_fasta(ref_fname)
coverage_data = preprocess_data(align_fname)

A = [40000749, 40000920, 40001316, 40001320, 40001324, 40001361, 40001472, 40001533, 40001541, 40001544, 40001997, 40002002] 

