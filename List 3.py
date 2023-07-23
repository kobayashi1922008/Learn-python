n = int(input("so item :"))
s = input("s =")
tong = 0
dem = 0
list = s.split()
if n==len(list):
  list = [int(item) for item in list] #ép kiểu dữ 

  for item in list:
    if item>0:
      tong += item
      dem+= 1
  print("Tong la:", tong)
  print("Co", dem ,"So duong")
else:
  print("Loi!")
