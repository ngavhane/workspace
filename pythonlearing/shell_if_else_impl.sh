echo "Enter 0 if you belongs to Calm.io"
echo "Enter 1 if you belongs to idea device"
echo "Enter 2 if you belongs to somewhere else"
read value
echo Option entered by user:$value
if test $value -eq 2; then 
	echo "User is from cisco"
else 
	if test $value -eq 1 ;then
 		echo "User is from idea device"
	else 
		echo "User is from calmio"
	fi

fi
