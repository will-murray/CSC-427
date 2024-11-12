#!/bin/bash -ue
bwa mem -t 8 /home/williammurray/CSC-427/A2/genome.fa /home/williammurray/CSC-427/A2/ENCSR000COQ1_1.fastq.gz /home/williammurray/CSC-427/A2/ENCSR000COQ1_2.fastq.gz > /home/williammurray/CSC-427/A2/genome.fa.sam
