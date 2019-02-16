def intreverse(n):
 res=0
 while(n > 0):
  lastDig = n %10
  res = res *10 + lastDig
  n = n //10
 return res 