num_list = [5, 1, 8, 92, -1, 30]

def search(list):
  print(num_list)
  kt = int(input("Nhập số mà bạn muốn ktra:"))
  if kt in num_list:
    print("số", kt, "có trong list và đứng số", num_list.index(kt))
  else:
    print("số", kt, "không có trong list")

def tinhtong(list):
  tong = 0
  print("Bạn muốn tính tổng bằng Function NUM hay Function FOR")
  print("1. là SUM")
  print("2. FOR")
  u_choose = int(input("Nhập số:"))
  if u_choose == 1:
    tinh_tong = sum(num_list)
    print("Tổng là", tinh_tong)
  else:
    for i in num_list:
      tong+=i
    print(tong)

while True:
  print("Menu:")
  print("1. là kiểm tra 1 số trong list")
  print("2. là tính tổng")
  print("3. OUT")
  u_choose = int(input("Chọn đi:"))
  if u_choose == 1:
    search(num_list)
  elif u_choose == 2:
    tinhtong(num_list)
  else:
    print("SAY BYEEEE")
    break
    