from __future__ import print_function

import os
import pava
import sys
import time

start = time.time()

sys.setrecursionlimit(100)

print('1. Number of loaded modules at start:',)
print(len(sys.modules))

# Tell pava where it can find Java user-defined classes
print('2. Loading Java...')
pava.set_classpath([os.path.join(os.path.dirname(__file__), "pava")])

print('3. Import the Python module that contains the transpiled HelloWorld...')
import helloworld

print('4. Call HelloWorld.main:')
print('#' * 80)
helloworld.HelloWorld.main__java_lang_String____([])

hi = helloworld.HelloWorld()
square = hi.square__int__(16)
print(square)
print('#' * 80)

print('5. Number of loaded modules after loading HelloWorld:')
print(len(sys.modules))

print('6. Done %.4fs.' % (time.time() - start))
