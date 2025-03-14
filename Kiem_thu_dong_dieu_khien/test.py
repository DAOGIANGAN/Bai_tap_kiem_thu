import pytest
from io import StringIO
import sys
from Kiem_thu_dong_dieu_khien import Total  # Import hàm từ file chính

@pytest.mark.parametrize("day, quantity, total, expected_output", [
    ("3/3", -1, 1000000, "Gia tri dau vao khong hop le!\n"),
    ("3/3", 1, 1, "Khong phai ngay giam gia! Tong hoa don: 1 dong\n"),
    ("14/2", 3, 2000000, "Tong hoa don: 1800000 dong\n"),
    ("14/2", 4, 1500000, "Tong hoa don: 1200000 dong\n"),
])
def test_total(day, quantity, total, expected_output):
    # Redirect stdout để kiểm tra output của hàm
    captured_output = StringIO()
    sys.stdout = captured_output

    # Gọi hàm
    Total(day, quantity, total)

    # Lấy output thực tế
    sys.stdout = sys.__stdout__  # Khôi phục stdout
    actual_output = captured_output.getvalue()

    # So sánh với kết quả mong đợi
    assert actual_output == expected_output