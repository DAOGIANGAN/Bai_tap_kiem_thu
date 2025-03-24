def Total(day: str, quantity: int, total: float):
    if quantity <= 0 or total <= 0:
        print("Gia tri dau vao khong hop le!")
        return

    if day == "14/2":
        a = 0.1
        if quantity > 3 and total >= 1000000:
            a += 0.1
        print(f"Tong hoa don: {int(total * (1 - a))} dong")
    else:
        print(f"Khong phai ngay giam gia! Tong hoa don: {int(total)} dong")

