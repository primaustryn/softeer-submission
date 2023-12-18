import sys

#1 N, K
N,K = list(map(int, (input()).split(' ')))

#2 S1~Sn
scores = list(map(int, (input()).split(' ')))

#3 Ai, Bi for i = 0~K
listA=[]
listB=[]
for i in range(0,K):
  A,B=list(map(int, input().split(' ')))
  listA.append(A)
  listB.append(B)

for i in range(0,K):
  score = 0
  for j in range(listA[i]-1, listB[i]):
    score += scores[j]
  print(format(score/(listB[i]-listA[i]+1),".2f"))
  
    

  