import unittest
from unittest.mock import mock_open, Mock, create_autospec, patch
from src.reader import Reader

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = Reader()

    def test_app_read_all(self):
        with patch('builtins.open', mock_open(read_data="some data")) as mockfile:
            self.assertEqual(self.app.read_all('file.txt'), "some data")
            mockfile.assert_called_with('file.txt', 'r')

    def test_app_new_line(self):
        with patch('builtins.open', mock_open(read_data="line1\n")) as mockfile:
            self.app.add_sth("file.txt", "line2")
            mockfile.assert_called_once_with("file.txt", "a")
            h = mockfile()
            h.write.assert_called_once_with("line2")

    def test_app_deletefile(self):
        spec = create_autospec(self.app)
        spec.delete("file.txt")
        spec.delete.assert_called_once_with("file.txt")

    def tearDown(self):
        self.app = None


if __name__ == "__main__":
    unittest.main()