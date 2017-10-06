#Read from the file transpose.txt and print its transposed content to stdout
#echo $m  
n=`head -1 transpose.txt | wc -w`  
for i in `seq $n`  
# get contents of a col and print as a row  
do  
  #echo `awk '{print $'$i'}' ORS="\t" $filename`  
	echo `awk -F " " 'BEGIN{ORS=" "}{print $'$i'}' transpose.txt`
done  
