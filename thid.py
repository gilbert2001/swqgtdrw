import os
try:
    from jnius import autoclass

except KeyError:
    os.environ['JDK_HOME'] = "/Users/mac/jdk-19_macos-aarch64_bin/jdk-19.0.2.jdk"
    os.environ['JAVA_HOME'] = "/usr/libexec/java_home"
    os.environ['JVM_PATH'] = "/Users/mac/Library/Java/JavaVirtualMachines/openjdk-17.0.1/Contents/Home/lib/libjvm.so"
    from jnius import autoclass
    Stack = autoclass('java.util.Stack')
    stack = Stack()
    stack.push('hello')
    stack.push('world')

    print( stack.pop()) # --> 'world'
    print( stack.pop()) # --> 'hello'