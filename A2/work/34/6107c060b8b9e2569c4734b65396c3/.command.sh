#!/bin/bash -ue
samtools view -S -b /home/williammurray/CSC-427/A2/genome.fa.sam > /home/williammurray/CSC-427/A2/genome.fa.bam
samtools sort /home/williammurray/CSC-427/A2/genome.fa.bam -o /home/williammurray/CSC-427/A2/genome.fa.sorted.bam
