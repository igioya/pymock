#import inspect
from collections import OrderedDict

class Mock(object):
	
	def __init__(self):
		self._msgs = OrderedDict() #Pair(message_name, [(*args, return_value)])
		self._have_params = dict()
		self._transaction = Transaction()
		#self._parent = class_to_mock

	def set_property(self, name_method):
		if self._transaction.aquire_transaction():
			print("SI")
			self._msgs[name_method] = OrderedDict()
			self._have_params[name_method] = False 
		else:
			#throw Error
			pass
		return self

	def with_params(self,*args):
		property_name = next(reversed(self._msgs.keys()))
		self._have_params[property_name] = True 
		#self._msgs[property_name] = (args, self._msgs[property_name].first()) 
		self._msgs[property_name][args] = "None" #Return Value
		print("DD:",self._msgs)
		#if self._have_params[]
		#self._msgs[]
		return self 

	def then(self, return_value):
		if not self._transaction.aquire_transaction():
			property_name = next(reversed(self._msgs.keys()))
			args = next(reversed(self._msgs[property_name].keys()))
			print("ARGS:",args)
			
			if self._have_params[property_name]:
				first = self._msgs[property_name][args]
				print("FIRST:",first)
				self._msgs[property_name][args] = return_value

		print("DD:",self._msgs)


	def __getattr__(self, property_name):
		def method_missing(*args, **kwargs):
			print('called %s with %d arguments %s & %d keywords %s' % (property_name, len(args), args, len(kwargs), kwargs))
			if self._have_params[property_name]:
				print("have params!")
				print(self._msgs[property_name])
				print(args)
				return_value_aux = None 
				for params, return_value in self._msgs[property_name].items():
				    if params == args:
				    	return_value_aux = return_value
				    	print("are equals!!")
			return return_value_aux
		return method_missing

class Transaction(object):
	def __init__(self):
		self._ticket = True
	pass

	def aquire_transaction(self):
		ticket = self._ticket 
		if self._ticket:
			self._ticket = False
		print("##Ticket:", ticket)
		return ticket 


# I name it set_property since in python all methods are properties

if __name__ == "__main__":
    mock = Mock()
    mock.set_property('get_count').with_params(2,4,3).then(200)
    print(mock.get_count(2,4,3) == 200)
