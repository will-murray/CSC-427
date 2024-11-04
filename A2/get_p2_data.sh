# this script was copied directly from the assignment pdf.

wget "https://github.com/nextflow-io/training/raw/refs/heads/master/hands-on/data/genome.fa"

for i in OQ1 OQ2; do for j in 1 2;
    do wget -c "https://github.com/nextflow-io/training/raw/refs/heads/master/hands-on/data/reads/ENCSR000C${i}_${j}.fastq.gz"; done; done