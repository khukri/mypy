import builtins

class Error(builtins.Exception):
	list __weakref__

t copy<t>(t x): pass

t deepcopy<t>(t x): pass
t deepcopy<t>(t x, dict memo): pass
t deepcopy<t>(t x, dict memo, list _nil): pass
