"""
Test suite cho Bụt Application
"""
import unittest
import sys
import os

# Thêm thư mục gốc vào path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from but_app import ButApp


class TestButApp(unittest.TestCase):
    """Test cases cho ButApp"""
    
    def setUp(self):
        """Khởi tạo trước mỗi test"""
        self.app = ButApp()
    
    def test_get_services(self):
        """Test lấy danh sách dịch vụ"""
        services = self.app.get_services()
        self.assertIsInstance(services, dict)
        self.assertEqual(len(services), 5)
        self.assertIn('an_uong', services)
        self.assertIn('di_lai', services)
        self.assertIn('thuoc_men', services)
        self.assertIn('viec_nha', services)
        self.assertIn('viec_nong', services)
    
    def test_request_service_an_uong(self):
        """Test yêu cầu dịch vụ ăn uống"""
        result = self.app.request_service('an_uong', 'Đặt cơm trưa')
        self.assertEqual(result['status'], 'success')
        self.assertEqual(result['service'], 'Dịch vụ ăn uống')
        self.assertEqual(result['description'], 'Đặt cơm trưa')
    
    def test_request_service_di_lai(self):
        """Test yêu cầu dịch vụ đi lại"""
        result = self.app.request_service('di_lai', 'Đặt xe đi sân bay')
        self.assertEqual(result['status'], 'success')
        self.assertEqual(result['service'], 'Dịch vụ đi lại')
    
    def test_request_service_thuoc_men(self):
        """Test yêu cầu dịch vụ thuốc men"""
        result = self.app.request_service('thuoc_men', 'Mua thuốc cảm')
        self.assertEqual(result['status'], 'success')
        self.assertEqual(result['service'], 'Dịch vụ thuốc men')
    
    def test_request_service_viec_nha(self):
        """Test yêu cầu dịch vụ việc nhà"""
        result = self.app.request_service('viec_nha', 'Dọn nhà')
        self.assertEqual(result['status'], 'success')
        self.assertEqual(result['service'], 'Dịch vụ việc nhà')
    
    def test_request_service_viec_nong(self):
        """Test yêu cầu dịch vụ việc nông"""
        result = self.app.request_service('viec_nong', 'Làm ruộng')
        self.assertEqual(result['status'], 'success')
        self.assertEqual(result['service'], 'Dịch vụ việc nông')
    
    def test_request_invalid_service(self):
        """Test yêu cầu dịch vụ không tồn tại"""
        result = self.app.request_service('invalid_service', 'Test')
        self.assertIn('không tồn tại', result)


if __name__ == '__main__':
    unittest.main()
