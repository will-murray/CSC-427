#!/bin/bash

# Download and decompress FASTQ file
wget -O "SRR800824_1.fastq.gz" "https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR800/SRR800824/SRR800824_1.fastq.gz" | gzip -d > SRR800824_1.fastq

# Define directory and file names
OUTPUT_DIR="p3_output"
FASTQ_FILE="SRR800824_1.fastq"
READS_FILE="$OUTPUT_DIR/reads.txt"
QUALS_FILE="$OUTPUT_DIR/quals.txt"
NAMES_FILE="$OUTPUT_DIR/names.txt"
FULL_FILE="$OUTPUT_DIR/full.txt"

mkdir -p $OUTPUT_DIR

# Create/empty the output files
> $READS_FILE
> $QUALS_FILE
> $NAMES_FILE
> $FULL_FILE

# Snippets of this code come from https://www.tutorialspoint.com/awk/index.htm
awk 'NR % 4 == 1 { 
        # Store read name
        read_name = substr($1, 2, length($1)); 
        split(read_name, name_parts, "."); 
        if (name_parts[length(name_parts)] % 8 == 0) {
            # If divisible by 8, store the read name
            names[count++] = read_name; 
            getline seq; 
            reads[count] = seq; 
            getline; 
            getline qual; 
            quals[count] = qual;
        }
    }
    END {
        for (i = 1; i <= count; i++) {
            print reads[i] >> "'$READS_FILE'";
            print quals[i] >> "'$QUALS_FILE'";
            print names[i] >> "'$NAMES_FILE'";
            print names[i], reads[i], quals[i] >> "'$FULL_FILE'";
        }
    }' $FASTQ_FILE
