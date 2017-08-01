#!/usr/bin/bash

# Math operation
# expr or []
#ARG1 | ARG2 Returns ARG1 if neither argument is null or zero; otherwise, returns ARG2
#ARG1 & ARG2 Returns ARG1 if neither argument is null or zero; otherwise, returns 0
#ARG1 < ARG2 Returns 1 if ARG1 is less than ARG2; otherwise, returns 0
#ARG1 <= ARG2 Returns 1 if ARG1 is less than or equal to ARG2; otherwise, returns 0
#ARG1 = ARG2 Returns 1 if ARG1 is equal to ARG2; otherwise, returns 0
#ARG1 != ARG2 Returns 1 if ARG1 is not equal to ARG2; otherwise, returns 0
#ARG1 >= ARG2 Returns 1 if ARG1 is greater than or equal to ARG2; otherwise,returns 0
#ARG1 > ARG2 Returns 1 if ARG1 is greater than ARG2; otherwise, returns 0
#ARG1 + ARG2 Returns the arithmetic sum of ARG1 and ARG2
#ARG1 - ARG2 Returns the arithmetic difference of ARG1 and ARG2
#ARG1 * ARG2 Returns the arithmetic product of ARG1 and ARG2
#ARG1 / ARG2 Returns the arithmetic quotient of ARG1 divided by ARG2
#ARG1 % ARG2 Returns the arithmetic remainder of ARG1 divided by ARG2
#STRING : REGEXP Returns the pattern match if REGEXP matches a pattern in STRING

#There are two ways to assign the output of a command to a variable
#The backtick character (`)
#The $() format
t1=`date`
t2=$(date +%Y-%m-%d)
echo $t1
echo $t2



#the expr command allowed the processing of equations from the command line, but it is extremely clunky:
var1=$(expr 1 + 5)
echo $var1
