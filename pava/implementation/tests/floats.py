import pava
import unittest

class FloatsTest(unittest.TestCase):
    def test_add(self):
        pava.run_java_test('float', 'return 1.0f + 1.0f;')  # Note: Javac optimizes constant expressions

        pava.run_java_test('float', 'float x = 1.0f; return x + 1.0f;')
        pava.run_java_test('float', 'float x = 1.0f; return x + 0.0f;')
        pava.run_java_test('float', 'float x = 0.0f; return x + 1.0f;')
        pava.run_java_test('float', 'float x = 0.0f; return x + 0.0f;')

        pava.run_java_test('float', 'float x = 1.0f; return x - 1.0f;')
        pava.run_java_test('float', 'float x = 1.0f; return x - 0.0f;')
        pava.run_java_test('float', 'float x = 0.0f; return x - 1.0f;')
        pava.run_java_test('float', 'float x = 0.0f; return x - 0.0f;')

        pava.run_java_test('float', 'float x = 1.0f; return x / 3;')

        pava.run_java_test('float', 'float x = 1.0f; x += 1.0f; return x;')
        pava.run_java_test('float', 'float x = 1.0f; x -= 1.0f; return x;')


if __name__ == "__main__":
    unittest.main()
