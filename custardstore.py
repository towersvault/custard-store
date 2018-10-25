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


import inspect


registered_class = None


def expose_function(function, *args):
	"""
	Adding this decorator to a function will
	expose it to custardstore. 
	Any arguments will be passed via *args.
	"""

	def fn(*args):
		try:
			return function(*args)
		except Exception as e:
			print('E', str(e))
	return fn


def register_class(cls):
	"""
	The submitted class will be initialized on
	a global variable.
	"""

	global registered_class
	registered_class = cls()


def call_function(function, *args):
	"""
	The custard of the custardstore.
	Any functions that needs to be called will pass through
	here.

	Usage Examples:
	call_function('hello_world')
		Calls registered_class.hello_world()

	call_function('foo', 'bar')
		Calls registered_class.foo('bar')
	"""

	global registered_class

	def is_a_function():
		sourcelines = inspect.getsourcelines(registered_class.__class__)[0]
		for i, line in enumerate(sourcelines):
			line = line.strip()
			if line.split('(')[0].strip() == '@expose_function':
				next_line = sourcelines[i + 1]
				name = next_line.split('def')[1].split('(')[0].strip()
				if name == function:
					return True
		return False
	
	if is_a_function():
		if len(args) > 0:
			fn = getattr(registered_class, function)
			return fn(*args)
		else:
			fn = getattr(registered_class, function)
			return fn()
	else:
		raise FunctionError(str(function) + ' does not exist or isn\'t exposed.')


class FunctionError(Exception):
	def __init__(self, message):
		super().__init__(message)