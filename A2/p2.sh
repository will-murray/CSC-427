#!/bin/bash

#usage: bash p2.sh genome.fa ENCSR000COQ1_1.fastq.gz ENCSR000COQ1_2.fastq.gz 2 result.vcf

if [ "$#" -ne 5 ]; then
    echo "Error: Exactly 5 arguments are required."
    exit 1
fi

ref_gn=$1
reads_1=$2
reads_2=$3
n_threads=$4
output_fname=$5

# Record the start time
start_time=$(date +%s)

# Index the reference genome
bwa index $ref_gn

# Align the paired-end reads to the reference index
bwa mem -t $n_threads $ref_gn $reads_1 $reads_2 > $ref_gn.sam

# Convert alignment to BAM
samtools view -S -b $ref_gn.sam > $ref_gn.bam

# Sort the alignment
samtools sort $ref_gn.bam -o $ref_gn.sorted.bam

# Call variants
bcftools mpileup -f $ref_gn $ref_gn.sorted.bam | \
bcftools call -mv -Ob | \
bcftools filter -i 'QUAL>=20 && INFO/DP>=20' -o $output_fname -O v

# Remove all files with prefix $ref_gn
rm "${ref_gn}"?*

# Record the end time
end_time=$(date +%s)

# Calculate and print the runtime
runtime=$((end_time - start_time))
echo "$n_threads : $runtime seconds"

# C)

# 1 thread : 43 seconds
# 2 threads : 43 seconds

# no speedup from 1 to 2 threads

#E)

# grep "^chr22" result.vcf | wc -l print 99


#F) 

#If this script is interruppted before its done execution, files created by bwa index are not removed. 
# when the script is rerun, it starts from the begginning and does not use files which have already been created.

# One solution, could be maintaining a stack of intermediate files to be deleted. When a keyboard interrupt occurs,
# files on the stack could be popped and removed

# Alternatively, when a keyboard interrupt occurs, a file could be kept
# to track where the execution can continue. This way, expensive steps dont have to be repeated.