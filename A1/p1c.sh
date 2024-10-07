awk '/^>/ {if (seq) print seq; print; seq=""; next} {seq=seq$0} END {if (seq) print seq}' sacCer3.fa > sacCer3.flat.fa
