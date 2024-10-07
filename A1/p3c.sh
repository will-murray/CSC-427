# this script assumes that the zipped versions of these files exist already
for file in names.txt full.txt quals.txt reads.txt
do 
    rm "p3_output/"$file".gz"
    gzip -k -9 "p3_output/"$file 
done
for file in names.txt full.txt quals.txt reads.txt
do 
    stat --format="%s" "p3_output/"$file".gz"
done


# The zipped file sizes in bytes are
# names.txt : 3750671
# full.txt : 115178497
# quals.txt : 56036578
# reads.txt : 44137647
#

# Using -<number> (0-9) species the speed of compression. Using -9 means that the 
# compression is slower but gets the highest compression ratio