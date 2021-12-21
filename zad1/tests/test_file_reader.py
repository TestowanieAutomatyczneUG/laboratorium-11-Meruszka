import unittest
from unittest.mock import mock_open, patch
from src.reader import Reader

class TestFileReader(unittest.TestCase):
    def setUp(self):
        self.reader = Reader()
