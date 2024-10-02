awk '/^>/ { if (seq) print seq; print; seq=""; next } { seq = seq $0 } END { if (seq) print seq }' saccer3.fa > sacCer3.flat.fa
