n = int(input("n = "))
check = 1

for i in range(2,n):
  if n%i==0:
    check = 0
    break
if check == 1:
  print("Yess")
else:
  print("NO")
