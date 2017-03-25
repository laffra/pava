# pava
Run code written in the Java Language on a Python VM

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
  * Loaded the class file
  * If needed create a placeholder Python module with the same name as the Java package
  * Generate a Python class in the module
  * Add a Python method for each Java method found
  * Transpile each of the Java bytecodes into the corresponding Python bytecodes
  * Add a Python class attribute for each Java field found
  * Handle &lt;init&gt; and &lt;clinit&gt; to properly initialize the Python fields
2. During runtime execution of the code:
  * Simply run the generated code.
  * Mimic the Java classloading behavior of triggering classes/modules
  
# Dependencies

Pava uses Jawa for analyzing the Java class files and Peak Bytecode Assembler to generate the Python bytecodes.
See:
* https://github.com/TkTech/Jawa
* http://peak.telecommunity.com/DevCenter/BytecodeAssembler

# Next steps
Pava is in very early stage of development. Next steps are:

- Implement native Java methods in Python, such as System.out.println needs.
- Handle clinit to properly intialize static fields.
- Handle overloaded Java methods.
- Write a lot of tests for rudimentary long/double/float/math operations.
- Generate Python *source*, rather than bytecodes, to more easily debug the transpiler.
- Run the test suite provided in the openjdk project.
