import sys

total_w,n = (input()).split(' ')
total_w = int(total_w)
tuples = []

for i in range(0,int(n)):
  w,p=(input()).split(' ')
  tuples.append((int(w),int(p)))

tuples = sorted(tuples, key=lambda x: x[1])
tuples.reverse()
# print(tuples)

sum_w=0
sum_p=0
for w,p in tuples:
  if sum_w + w >= total_w:
    w_partial = total_w - sum_w
    sum_p += p * w_partial
    sum_w += w_partial
  else : 
    sum_p += p * w
    sum_w += w
  if sum_w == total_w:
    break  
print(sum_p)