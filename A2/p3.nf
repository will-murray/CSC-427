nextflow.enable.dsl=2

params.base_dir = "$baseDir"  // Base directory, automatically set in Nextflow

process buildIndex {

    output:
    stdout

    script:
    """
    bwa index ${params.base_dir}/${params.reference}
    """
}

process alignReads {

    input:
    stdin
    
    output:
    stdout

    script:
    """
    bwa mem -t ${params.threads} ${params.base_dir}/${params.reference} ${params.base_dir}/${params.files.replace('*', '1')} ${params.base_dir}/${params.files.replace('*', '2')} > ${params.base_dir}/${params.reference}.sam
    """
}

process sortAndConvert{

    input:
    stdin

    output:
    stdout

    script:
    """
    samtools view -S -b ${params.base_dir}/${params.reference}.sam > ${params.base_dir}/${params.reference}.bam
    samtools sort ${params.base_dir}/${params.reference}.bam -o ${params.base_dir}/${params.reference}.sorted.bam
    """

}

process callVariants{
    input:
    stdin

    output:
    stdout

    script:
    """
    bcftools mpileup -f ${params.base_dir}/${params.reference} ${params.base_dir}/${params.reference}.sorted.bam | \
    bcftools call -mv -Ob | \
    bcftools filter -i 'QUAL>=20 && INFO/DP>=20' -o ${params.base_dir}/${params.output} -O v
    """
}

process cleanup {
    input:
    stdin

    script:
    """
    rm "${params.base_dir}/${params.reference}"?*
    """
}

workflow{
    // buildIndex()
    alignReads(params.output)
    sortAndConvert(alignReads.out.collect())
    callVariants(sortAndConvert.out.collect())
    cleanup(callVariants.out.collect())
}