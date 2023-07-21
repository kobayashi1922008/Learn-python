n = int(input("so item :"))
s = input("s =")
tong = 0
dem = 0
list = s.split()
list = [int(item) for item in list]

for item in list:
  if item>0:
    tong += item
    dem+= 1

print("Tong la:", tong)
print("Co", dem ,"So duong")