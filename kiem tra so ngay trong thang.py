month = int(input("Hay nhap thang :"))

if month in (1,3,5,7,8,10,12):
  print("31 ngay")
elif month in (4,6,9,11):
  print("30 ngay")
elif month == 2:
  year = int(input("Hay nhap nam :"))
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("29 ngay")
  else:
    print("28 ngay")