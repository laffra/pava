import pava
import unittest

class ArrayTest(unittest.TestCase):
    def test_add(self):
        pava.run_java_test('int', 'int[] x = new int[5]; return x[1];')
        pava.run_java_test('int', 'int[] x = new int[5]; return x.length;')
        pava.run_java_test('int', 'int[] x = new int[5]; x[1] = 2; return x[1];')
        pava.run_java_test('int', 'int[] x = new int[5]; x[3] = 4; return x[0] + x[3];')

def main():
    unittest.main()

if __name__ == "__main__":
    main()
