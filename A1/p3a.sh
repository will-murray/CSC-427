#!/bin/bash

# Download and unpack the FASTQ file
echo "Downloading SRR800824 FASTQ file..."
fastq_url="ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR800/SRR800824/SRR800824_1.fastq.gz"
output_fastq="SRR800824_1.fastq.gz"
wget -O $output_fastq $fastq_url

# Unzip the file
echo "Unpacking the FASTQ file..."
gunzip $output_fastq

# Initialize output files
echo "Creating output files..."
> reads.txt
> quals
