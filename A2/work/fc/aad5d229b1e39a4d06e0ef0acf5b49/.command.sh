#!/bin/bash -ue
bcftools mpileup -f /home/williammurray/CSC-427/A2/genome.fa /home/williammurray/CSC-427/A2/genome.fa.sorted.bam |     bcftools call -mv -Ob |     bcftools filter -i 'QUAL>=20 && INFO/DP>=20' -o /home/williammurray/CSC-427/A2result.vcf -O v
