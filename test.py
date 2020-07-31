import unittest
from unittest import mock
from main import wait_until


class TestApp(unittest.TestCase):

    @mock.patch('main.MyThread.is_alive', return_value=False)
    def test_0010_add(self, _is_alive):
        result = wait_until()
        self.assertEqual(1, 1)


def suite():
    suite = unittest.TestSuite()
    suite.addTests(
        unittest.TestLoader().loadTestsFromTestCase(TestApp)
    )
    return suite


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())