awk '/CGCGCGCGCG/{print prev} {prev=$0}' sacCer3.flat.fa
