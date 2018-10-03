import inspect

class Mock(object):
	
	def __init__(self):
		self._msgs = dict()
		#self._parent = class_to_mock

	def when_its_called(self, name_method, return_value):
		self._msgs[name_method] = return_value
		return self

	def __getattr__(self, name):
		def method_missing(*args, **kwargs):
			#'called %s with %d arguments %s & %d keywords %s' % (name, len(args), args, len(kwargs), kwargs)
			return self._msgs[name]
		return method_missing

		


if __name__ == "__main__":
    mock = Mock()
    mock.when_its_called('papa', 'pepe')
    print(mock.papa())
