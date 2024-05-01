import unittest
from MyTestRunner import MyTextTestRunner
class Login(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass
    def test_1(self):
        """測試-a"""
        b=False
        self.assertEqual(b,True)
    def test_2(self):
        """測試-b"""
        a=True
        self.assertEqual(a, True)

    def test_3(self):
        """測試-c"""
        data=4/0

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Login))
    runner = MyTextTestRunner()
    runner.run(suite)