import sys

n = eval(input())
# print(n)

for i in range(0,n):
  A_B=input()
  a,b = A_B.split(' ')
  print("Case #"+str(i+1) +": " + str(int(a)+int(b)))