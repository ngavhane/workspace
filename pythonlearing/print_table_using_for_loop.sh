if $# -eq 0
then
   echo "No arguments passed ,so no table will be printed"
exit 1
fi
for i in 1 2 3 4 5 6 7 8 9 10
do 
	echo "$1 * $i = `expr $1 \* $i`"
done

