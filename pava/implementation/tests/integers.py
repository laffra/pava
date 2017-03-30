import pava
import unittest

class IntegersTest(unittest.TestCase):
    def test_add(self):
        pava.run_java_test('int', 'return 1 + 1;')  # Note: Javac optimizes constant expressions

        pava.run_java_test('int', 'int x = 1; return x + 1;')
        pava.run_java_test('int', 'int x = 1; return x + 0;')
        pava.run_java_test('int', 'int x = 0; return x + 1;')
        pava.run_java_test('int', 'int x = 0; return x + 0;')

        pava.run_java_test('int', 'int x = 1; return x - 1;')
        pava.run_java_test('int', 'int x = 1; return x - 0;')
        pava.run_java_test('int', 'int x = 0; return x - 1;')
        pava.run_java_test('int', 'int x = 0; return x - 0;')

        pava.run_java_test('int', 'int x = 1; x += 1; return x;')
        pava.run_java_test('int', 'int x = 1; x -= 1; return x;')

        pava.run_java_test('int', 'int x = 6; return x / 2;')
        pava.run_java_test('int', 'int x = 5; return x / 2;')
        pava.run_java_test('int', 'int x = 4; return x / 2;')
        pava.run_java_test('int', 'int x = 3; return x / 2;')
        pava.run_java_test('int', 'int x = 2; return x / 2;')
        pava.run_java_test('int', 'int x = 1; return x / 2;')

if __name__ == "__main__":
    unittest.main()
