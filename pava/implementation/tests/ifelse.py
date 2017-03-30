import pava
import unittest

class IfElseTest(unittest.TestCase):
    def test_add(self):
        pava.run_java_test('int', 'boolean x=true; if (x) { return 1; } else { return 2;}')
        pava.run_java_test('int', 'boolean x=false; if (x) { return 1; } else { return 2;}')
        pava.run_java_test('int', 'boolean x=true; if (!x) { return 1; } else { return 2;}')
        pava.run_java_test('int', 'boolean x=false; if (!x) { return 1; } else { return 2;}')

if __name__ == "__main__":
    unittest.main()
