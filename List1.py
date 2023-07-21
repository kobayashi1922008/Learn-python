n = int(input("n =:"))
s = input("nhap list:")
list = s.split()
if n == len(list):
  x = input("x =:")
  count = list.count(x)
  print(count)
else:
  print("Loi")