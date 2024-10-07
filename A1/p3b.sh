for file in names.txt full.txt quals.txt reads.txt
do 
    gzip -k "p3_output/"$file 
done
for file in names.txt full.txt quals.txt reads.txt
do 
    stat --format="%s" "p3_output/"$file".gz"
done


# The zipped file sizes in bytes are
# names.txt : 3786383
# full.txt : 117458527
# quals.txt : 57292568
# reads.txt : 45938921
#
# The combined size of quals, names and reads is 107017872 which is 91% of full.txt
# It is better to compress the parts individually since gzip works better when similiar items are grouped