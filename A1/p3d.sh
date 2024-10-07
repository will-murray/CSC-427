# this script assumes that the zipped versions of these files exist already
for file in names.txt full.txt quals.txt reads.txt
do 
    bzip2 -k "p3_output/"$file 
done
for file in names.txt full.txt quals.txt reads.txt
do 
    stat --format="%s" "p3_output/"$file".bz2"
done


#bzip2 is a BWT algorithm and does better than gzip -9 for these specific files
# The improvement in compression ratio is due to the fact that BWT takes advantage of 
# similiarities in the data even if the data wasn't sorted so that similiar data is grouped together