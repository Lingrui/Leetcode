#Read from the file file.txt and output the tenth line to stdout
#Solution1 
awk 'NR == 10' file.txt
#Solution2
awk '{if(NR == 10) print $0}' file.txt 

#Solution3 
sed -n 10p file.txt

