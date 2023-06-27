year = int(input("Hay chon nam ma ban muon kiem tra :"))

if (year / 4 == 0 and year / 100 != 0) or (year / 100 == 0 and year / 400  == 0):
    print("Nam", year("la nam nhuan"))
else:
    print("Nam", year("khong phai la nam nhuan"))