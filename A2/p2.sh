#usage: bash p2.sh genome.fa ENCSR000COQ1_1.fastq.gz ENCSR000COQ1_2.fastq.gz 2 result.vcf

ref_gn=$1
reads_1=$2
reads_2=$3
n_threads=$4
output_fname=$5

#index the reference genome
bwa index $ref_gn
# align the paired end reads to the reference index
bwa mem -t $n_threads $ref_gn $reads_1 $reads_2 > $ref_gn.sam

# convert alignment to bam
samtools view -S -b $ref_gn.sam > $ref_gn.bam

# sort the alignment
samtools sort $ref_gn.bam -o $ref_gn.sorted.bam

bcftools mpileup -f $ref_gn $ref_gn.sorted.bam | \
bcftools call -mv -Ob | \
bcftools filter -i 'QUAL>=20 && INFO/DP>=20' -o $output_fname -O v

#remove all files which have prefix $ref_gn
rm "${ref_gn}"?*
