n = int(input("Nhap so item:"))
s = input("Nhap item")
list = s.split()

if n==len(list):
  list = [int(item) for item in list]
  set = set(list) # set như là 1 biến, đôi lúc tự sắp xếp từ bé đến lớn
  print(set)
else:
  print("Loi, nhap lai")