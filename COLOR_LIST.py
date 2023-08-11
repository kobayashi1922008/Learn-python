colors_list = ["red", "blue", "teal", "green"]

def print_a_color(colors_list):
  vi_tri = input("Chọn vị trí trong list")
  print("Màu bạn chọn là :", (colors_list[int(vi_tri)]))

def delete(colors_list):
  delete1 = input("Nhập color mà bạn muốn xóa :")
  if delete1.isdigit() == True:
    colors_list.pop(int(delete1))
  else:
    colors_list.remove(delete1)
def print_color(colors_list):
  print("List của bạn sẽ như sau", ", ".join(colors_list))
  
while True:
  print("Menu user:")
  print("1. Xem 1 color theo vi tri")
  print("2. Delete 1 color ")
  print("3. Out chuong trinh")
  u_choose = int(input("Nhap so:"))
  if u_choose == 1:
    print_a_color(colors_list)
  elif u_choose == 2:
    delete(colors_list)
    print_color(colors_list)
  else:
    print("đang tắt chương trình")
    break
