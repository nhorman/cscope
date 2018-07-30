#!/bin/sh
EXPECT=3
SINDEX=4
STERM=oldsigquit
STYPE="regular text string"

echo "Searching item $SINDEX, '$STYPE'"

#Get to the top level directory
cd ..

#Remove any previous databases from testing
rm -f cscope.out

COUNT=$(./src/cscope -R -L -$SINDEX$STERM | wc -l)

if [ $COUNT -ne $EXPECT ]
then
	echo "Expected $EXPECT instances of $STYPE $STERM but found $COUNT"
	exit 1
fi

exit 0

