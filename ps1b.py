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
  
high = 10000
low = 1
Trial = (high + low)/2.0

while formuladivT * Trial != B:
  if formuladivT * Trial < B:
    low = Trial
  else:
    high = Trial
  Trial = (high + low)/2.0

if formuladivT * int(Trial) < B:
  Trial = int(Trial) + 1
else:
  pass

T = Trial

# please do not modify the input and print statements
# and make sure that your code does not have any other print statements
print(T)