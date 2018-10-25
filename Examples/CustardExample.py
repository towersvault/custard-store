#!/usr/bin/env python3

__copyright__ = '''
	Copyright 2018 Clifford Steyn <clifford@softwxre.io>
	Licensed under the Apache License, Version 2.0 (the "License");
	you may not use this file except in compliance with the License.
	You may obtain a copy of the License at
		http://www.apache.org/licenses/LICENSE-2.0
	Unless required by applicable law or agreed to in writing, software
	distributed under the License is distributed on an "AS IS" BASIS,
	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	See the License for the specific language governing permissions and
	limitations under the License.
	'''
__license__ = 'Apache 2.0'


import custardstore
from custardstore import expose_function


class ExampleClass:
	def __init__(self):
		pass

	@expose_function
	def hello_world(self):
		"""
		This function just prints something out.
		"""
		print('Hello World')
	
	@expose_function
	def foo(self):
		"""
		This function returns a variable.
		"""
		return 'bar'

	@expose_function
	def add_these(self, a, b):
		"""
		This function takes 2 variables and returns the result.
		"""
		c = a + b
		return c

	def i_am_hidden(self):
		"""
		This function is hidden, calling it won't work.
		"""
		print('How can you see me??')


if __name__ == '__main__':
	# Register a class that custard_store will use.
	custardstore.register_class(ExampleClass)

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