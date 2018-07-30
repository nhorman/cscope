#!/bin/sh

EXPECT=3
SINDEX=1
STERM=main
STYPE="symbol definition"

echo "Searching item $SINDEX, '$STYPE'"

#Get to the top level directory
cd ..

#Remove any previous databases from testing
rm -f cscope.out

#Count the number of instances of the string 'Copyright'
#We expect 178 currently
COUNT=$(./src/cscope -R -L -$SINDEX$STERM | wc -l)

if [ $COUNT -ne $EXPECT ]
then
	echo "Expected $EXPECT instances of $STYPE $STERM but found $COUNT"
	exit 1
fi

exit 0

