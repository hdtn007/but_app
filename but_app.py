#!/usr/bin/env python3
"""
Bụt Application - Hệ thống hỗ trợ các nhu cầu trong cuộc sống
"""

class ButApp:
    """
    Bụt Application - Lo hết mọi thứ trong cuộc sống
    """
    
    def __init__(self):
        self.services = {
            'an_uong': 'Dịch vụ ăn uống',
            'di_lai': 'Dịch vụ đi lại', 
            'thuoc_men': 'Dịch vụ thuốc men',
            'viec_nha': 'Dịch vụ việc nhà',
            'viec_nong': 'Dịch vụ việc nông'
        }
    
    def get_services(self):
        """Lấy danh sách các dịch vụ"""
        return self.services
    
    def request_service(self, service_type, description):
        """Yêu cầu dịch vụ"""
        if service_type not in self.services:
            return f"Dịch vụ '{service_type}' không tồn tại"
        
        return {
            'status': 'success',
            'service': self.services[service_type],
            'description': description,
            'message': f'Đã tiếp nhận yêu cầu {self.services[service_type]}: {description}'
        }
    
    def display_menu(self):
        """Hiển thị menu dịch vụ"""
        print("\n=== HỆ THỐNG BỤT APPLICATION ===")
        print("Lo hết mọi thứ trong cuộc sống\n")
        print("Các dịch vụ có sẵn:")
        for key, value in self.services.items():
            print(f"  - {key}: {value}")
        print()


def main():
    """Hàm chính chạy ứng dụng"""
    app = ButApp()
    app.display_menu()
    
    # Demo các dịch vụ
    print("=== DEMO CÁC DỊCH VỤ ===\n")
    
    # Dịch vụ ăn uống
    result = app.request_service('an_uong', 'Đặt cơm trưa cho 4 người')
    print(result['message'])
    
    # Dịch vụ đi lại
    result = app.request_service('di_lai', 'Đặt xe từ nhà đến sân bay')
    print(result['message'])
    
    # Dịch vụ thuốc men
    result = app.request_service('thuoc_men', 'Mua thuốc cảm cúm')
    print(result['message'])
    
    # Dịch vụ việc nhà
    result = app.request_service('viec_nha', 'Dọn dẹp nhà cửa')
    print(result['message'])
    
    # Dịch vụ việc nông
    result = app.request_service('viec_nong', 'Thuê người làm ruộng')
    print(result['message'])
    

if __name__ == '__main__':
    main()
