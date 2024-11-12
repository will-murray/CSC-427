curl -L http://hgdownload.soe.ucsc.edu/goldenPath/hg19/chromosomes/chr22.fa.gz |gunzip -c > chr22.fa


samtools view -h -o testt.sam \
  https://ftp-trace.ncbi.nih.gov/1000genomes/ftp/phase3/data/HG00275/alignment/HG00275.mapped.ILLUMINA.bwa.FIN.low_coverage.20120522.bam \
  22:40000000-40002000

awk '{ if ($1 !~ /^@/) $3 = "chr" $3; print }' testt.sam > test.sam
rm testt.sam