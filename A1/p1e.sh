awk '/^>/ {print} !/^>/ {print $1; print $2 | "rev | tr \"ACGTacgt\" \"TGCAtgca\""}' sacCer3.flat.fa | fold -w 80 > sacCer3.rc.fa


