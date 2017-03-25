import pava


# Tell pava where it can find Java user-defined classes
pava.set_classpath(['c:/Users/laffr/PycharmProjects/pava/pava'])

try:
    import java
    class Out(object):
        def println(self, s):
            print s
    java.lang.System.out = Out()
except ImportError:
    pass


# Load a Java class and call a static method on it from Python

import classfiles
classfiles.HelloWorld.main()

