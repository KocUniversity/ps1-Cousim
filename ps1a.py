n, B = list(map(int, input().strip().split()))
T = 0

# your code here
T = 1
formuladivT = 0
for i in range(1, n+1):
  if (i) % 2 == 0:
    pint = 2**(i) + 1
  else:
    pint = 3**(i) + 1 
  formuladivT += pint**(n - i)
  
while formuladivT * T < B:
  T += 1

if T > 10000:
  T = -1
else:
  pass

# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
print(T)