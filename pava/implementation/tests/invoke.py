import pava
import unittest


TEST = '''
    String x = PavaTest.hello(0, 0);
    String y = new PavaTest().world;
    return x + y;
  }
  public String world = "World";
  public String foo(String p) {
    return p;
  }
  public static String hello(int x1, int x2) {
    return "Hello";
'''

class InvokeTest(unittest.TestCase):
    def test_add(self):
        pava.run_java_test('String', TEST)

if __name__ == "__main__":
    unittest.main()

