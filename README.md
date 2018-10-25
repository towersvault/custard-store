# custard-store :custard:
An easy way to run functions from a class by passing a few string variables.

# Usage
Import the needed stuff:
```python3
import custardstore
from custardstore import expose_function
```

Create a class and expose some functions:
```python3
class ExampleClass:
	def __init__(self):
		pass

	@expose_function
	def hello_world(self):
		print('Hello World')
	
	@expose_function
	def foo(self):
		return 'bar'

	@expose_function
	def add_these(self, a, b):
		c = a + b
		return c

	def i_am_hidden(self):
		print('How can you see me??')
```

Tell custardstore about the class:
```python3
custardstore.register_class(ExampleClass)
```

Calling a function can be done by doing the following:
```python3
# The following function will call ExampleClass.hello_world()
custardstore.call_function('hello_world')

# The following function will call ExampleClass.foo() and
# print the returned string.
return_foo = custardstore.call_function('foo')
print(return_foo)

# The following function will call ExampleClass.add_these(a, b)
# with 2 numbers and print the returned integer.
return_add_these = custardstore.call_function('add_these', 2, 4)
print(return_add_these)

# The following function will call ExampleClass.i_am_hidden()
# It won't work. FunctionError will be raised.
custardstore.call_function('i_am_hidden')
```

# License
custardstore is licensed under the Apache 2 License, meaning you can use it free of charge, without strings attached in commercial and non-commercial projects. 
