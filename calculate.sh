PREFIX='1_ab'
cd $PREFIX && python3 submission.py < input  > output
diff output answer
if [ $? != 0 ]
then echo 'wrong answer'
else echo 'you`re right.'
fi