from collections import namedtuple,Mapping

# Modified from: https://stackoverflow.com/questions/11351032/namedtuple-and-default-values-for-optional-keyword-arguments
def namedtuple_with_defaults(typename, field_names, default_values=()):
	T = namedtuple(typename, field_names, verbose=False)
	T.__new__.__defaults__ = (None,) * len(T._fields)
	if isinstance(default_values, Mapping):
		prototype = T(**default_values)
	else:
		prototype = T(*default_values)
	T.__new__.__defaults__ = tuple(prototype)
	return T