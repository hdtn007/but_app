# Bụt Application - Lo hết mọi thứ

Hệ thống ứng dụng hỗ trợ các nhu cầu trong cuộc sống, bao gồm ăn uống, đi lại, thuốc men, việc nhà, việc nông - tất cả mọi việc đều có thể dùng Bụt để giải quyết.

## Tính năng

### 1. Dịch vụ Ăn uống (`an_uong`)
- Đặt đồ ăn online
- Giao đồ ăn tận nơi
- Đặt bàn nhà hàng
- Tìm quán ăn gần đây

### 2. Dịch vụ Đi lại (`di_lai`)
- Đặt xe taxi/grab
- Thuê xe tự lái
- Đặt vé máy bay
- Đặt vé tàu/xe khách

### 3. Dịch vụ Thuốc men (`thuoc_men`)
- Mua thuốc online
- Tư vấn sức khỏe
- Đặt lịch khám bệnh
- Giao thuốc tận nơi

### 4. Dịch vụ Việc nhà (`viec_nha`)
- Dọn dẹp nhà cửa
- Giặt ủi quần áo
- Sửa chữa điện nước
- Chăm sóc vườn tược

### 5. Dịch vụ Việc nông (`viec_nong`)
- Thuê máy móc nông nghiệp
- Thuê người làm ruộng
- Tư vấn kỹ thuật trồng trọt
- Mua bán nông sản

## Cài đặt

```bash
# Clone repository
git clone https://github.com/hdtn007/but_app.git
cd but_app

# Chạy ứng dụng
python3 but_app.py
```

## Sử dụng

### Chạy demo ứng dụng
```bash
python3 but_app.py
```

### Chạy tests
```bash
python3 test_but_app.py
```

## Ví dụ sử dụng

```python
from but_app import ButApp

# Khởi tạo ứng dụng
app = ButApp()

# Xem danh sách dịch vụ
services = app.get_services()
print(services)

# Yêu cầu dịch vụ ăn uống
result = app.request_service('an_uong', 'Đặt cơm trưa cho 4 người')
print(result['message'])

# Yêu cầu dịch vụ đi lại
result = app.request_service('di_lai', 'Đặt xe từ nhà đến sân bay')
print(result['message'])

# Yêu cầu dịch vụ thuốc men
result = app.request_service('thuoc_men', 'Mua thuốc cảm cúm')
print(result['message'])

# Yêu cầu dịch vụ việc nhà
result = app.request_service('viec_nha', 'Dọn dẹp nhà cửa')
print(result['message'])

# Yêu cầu dịch vụ việc nông
result = app.request_service('viec_nong', 'Thuê người làm ruộng')
print(result['message'])
```

## Cấu trúc dự án

```
but_app/
├── README.md           # Tài liệu hướng dẫn
├── but_app.py          # Mã nguồn chính
├── config.json         # File cấu hình dịch vụ
└── test_but_app.py     # Test cases
```

## Phát triển

Dự án được xây dựng với Python 3 và có thể mở rộng thêm nhiều dịch vụ khác tùy theo nhu cầu.

## Đóng góp

Mọi đóng góp đều được hoan nghênh. Vui lòng tạo pull request hoặc mở issue để thảo luận.

## Giấy phép

MIT License
