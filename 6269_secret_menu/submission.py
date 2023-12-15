import sys

M,N,K = (input()).split(' ')

secret_numbers=[]
secret_numbers=list(map(int,input().split(' ')))

# print(secret_numbers)

input_numbers=[]

input_numbers=list(map(int,input().split(' ')))

# print(input_numbers)

flag_secret = False

for i in range(0,int(N)-int(M)):
  if input_numbers[i] == secret_numbers[0]:
    # print(str(input_numbers[i]) + ": in the check loop")
    count_match = 1
    for j in range(1, int(M)):
      if secret_numbers[j] == input_numbers[i+j]:
        count_match += 1
        # print("matched - secret : " + str(secret_numbers[j]) + " / input : " + str(input_numbers[i+j]))
      else:
        count_match = 0
        # print("different - secret : " + str(secret_numbers[j]) + " / input : " + str(input_numbers[i+j]))
        break
      if count_match == int(M):
        flag_secret = True
        
  # print(str(input_numbers[i]) + ": passed")

print("normal" if flag_secret is False else "secret")