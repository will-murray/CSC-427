grep -B 1 "CGCGCGCGCG" output.fa | grep "^>" | sed 's/^>//' | sort -u 