import pava
import unittest

import dis

import java
print java.lang.StringBuilder.__init__

class StringsTest(unittest.TestCase):
    def test_add(self):
        pava.run_java_test('String', 'String x = ""; return x;')
        pava.run_java_test('String', 'String x = "Hello World"; return x;')
        pava.run_java_test('String', 'String x = "Hello", y = "World"; return x + y;')

if __name__ == "__main__":
    unittest.main()
