import pava
import unittest

import dis
def foo():
    return int(1.0)
dis.dis(foo)

class ConversionTest(unittest.TestCase):
    def test_add(self):
        pava.run_java_test('int', 'float x = 1.0f; return (int)x;')
        pava.run_java_test('int', 'double x = 1.0; return (int)x;')
        pava.run_java_test('int', 'long x = 1L; return (int)x;')
        pava.run_java_test('int', 'int x = 1; return (int)x;')

        pava.run_java_test('float', 'double x = 1.0; return (float)x;')
        pava.run_java_test('float', 'float x = 1.0f; return (float)x;')
        pava.run_java_test('float', 'long x = 1L; return (float)x;')
        pava.run_java_test('float', 'float x = 1; return (float)x;')

if __name__ == "__main__":
    unittest.main()
