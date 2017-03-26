# Pava
Run Java in Python

# Goals
Pava loads Java class files, converts the bytecodes to Python bytecodes, and allows you to run the original Java code inside the Python VM. It is a mirror of Jython, in the sense that with Pava, Python is the dominant language. Pava converts all the Java bytecodes, including the entire Java runtime in rt.jar, caches the result, and allows you to use Java classes as if they were implemented in Python directly.

# Example Hello World
Assuming we have a Java example looking like this:

    public class HelloWorld {
        public static void main(String[] args) {
            System.out.println("Hello World!");
        }
    }
    
This Java code can be invoked unchanged using Pava as follows:

    import pava
    pava.set_classpath(['...the location of the Java classfiles...'])
    HelloWorld.main()
    
This prints:

    Hello World!
    
# How does Pava work?

Pava execution happens in two steps:
1. The Java classpath is processed. For each class file found on the classpath:
  * Load the class file
  * If needed, create a Python module with the same name as the Java package
  * Generate a Python class in the module
  * Add a Python method for each Java method found
  * Transpile each of the Java bytecodes into the corresponding Python bytecodes
  * Add a Python class attribute for each Java field found
  * Handle &lt;init&gt; and &lt;clinit&gt; to properly initialize the Python fields
2. During runtime execution of the code:
  * Simply run the generated code, which is now regular Python code.
  * Mimic the Java classloading behavior of triggering classes/modules
 
# Compilation of HelloWorld

The resulting Python bytecodes for HelloWorld are shown below, with their corresponding Java originals:

    Python Bytecodes generated by Pava        Original Java bytecodes in HelloWorld.class
    ---------------------------------------------------------------------------------------------------------------
     0 LOAD_GLOBAL    0 java            ###   0 getstatic ('java/lang/System', 'Ljava/io/PrintStream;', 'out')
     3 LOAD_ATTR      1 lang
     6 LOAD_ATTR      2 System
     9 LOAD_ATTR      3 out
    12 LOAD_ATTR      4 println
    15 LOAD_CONST     1 u'Hello World!' ###   3 ldc (u'Hello World!',)
    18 CALL_FUNCTION  1                 ###   5 invokevirtual ('java/io/PrintStream', 'println', 
                                                                                         '(Ljava/lang/String;)V', 1)
    21 POP_TOP
    22 LOAD_CONST    2 0                ###   8 return ()
    25 RETURN_VALUE
    -----------------------------------------------------------------------------------------------------------------

As you can observe, a static field in a Java class, such as "out" in "System", is retrieved as a regular attribute in Python. The class itself is part of a Java package, which equates to a module in Python, which is found by first loading the module called "java". From that, the module "lang" is found as an attribute on the "java" module.

Also interesting to note is that in Python, functions are invoked by placing the function on the stack first, followed by the arguments, following by the CALL_FUNCTION bytecode. Java uses a different order. Arguments come first, and the INVOKEVIRTUAL bytecode has an entry into the constant pool to find the actual function to invoke. Pava has to rearrange the stack as a result.

Finally, the HelloWorld.main method is a void function. In other words, it does not return anything. In Python, however, all functions return a result, where the default return value is None. Therefore, Pava inserts the required return value for void functions. Similarly, the "println" method is also a void function. This is why a POP_TOP is inserted at bytecode 21.

# Sample Transpilation Rules

Here are just a few examples from implementation/opcodes.py that impement the actual transpilation from Java bytecodes to Python bytecodes:

    def convert_ldc(code, java_pos, java_locals, value):
        code.LOAD_CONST(value)
        code.word_size = 1
        
    def convert_iinc(code, java_pos, java_locals, index, value):
        asm.Local(java_locals[index], code)
        code(asm.Const(value))
        code.BINARY_ADD()
        asm.LocalAssign(java_locals[index], code)
        code.word_size = 1
       
    def convert_dup2_x1(code, java_pos, java_locals):
        if code.word_size == 2:
            # before: word1, word2, ...
            code.DUP_TOP()
            code.ROT_THREE()
            # after: word1, word2, word1, ...
        else:
            # before: word1, word2, word3, ...
            code.ROT_TWO()
            code.DUP_TOP()
            code.ROT_FOUR()
            # now: word2, word1, word3, word2, ...
            code.ROT_TWO()
            code.DUP_TOP()
            code.ROT_FOUR()
            # after: word1, word2, word3, word1, word2, ...
     
    def convert_return(code, java_pos, java_locals):
        # an empty return in Java means return None in Python
        code.LOAD_CONST(0)
        code.RETURN_VALUE()
        code.set_stack_size(0)
        code.word_size = 0

# Dependencies

Pava uses Jawa for analyzing the Java class files and Peak Bytecode Assembler to generate the Python bytecodes.
See:
* https://github.com/TkTech/Jawa
* http://peak.telecommunity.com/DevCenter/BytecodeAssembler

# Next steps
Pava is in very early stage of development. Next steps are:

- Implement remaining bytecodes, such as multianewarray
- Fix stack underflow
- Implement native Java methods in Python, such as System.out.println needs.
- Handle clinit to properly intialize static fields.
- Make module loading more lazy, HelloWorld now loads 170 thousand methods.
- Handle overloaded Java methods.
- Write a lot of tests for rudimentary long/double/float/math operations.
- Generate Python *source*, rather than bytecodes, to more easily debug the transpiler.
- Run the test suite provided in the openjdk project.
