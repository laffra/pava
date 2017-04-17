import pava
import unittest
import sys

sys.setrecursionlimit(100)

class StringsTest(unittest.TestCase):
    def test_add(self):
        pava.run_java_test('String', '''
            String s = "Hello World";
            int len = s.length();
            char value[] = new char[len];
            s.getChars(0, len, value, 0);
            return "" + value[4];
        ''')
        return
        pava.run_java_test('String', 'String x = "Hello World"; return x;')
        pava.run_java_test('String', 'String x = ""; return x;')
        pava.run_java_test('String', 'String x = "Hello", y = "World"; return x + y;')

if __name__ == "__main__":
    unittest.main()


