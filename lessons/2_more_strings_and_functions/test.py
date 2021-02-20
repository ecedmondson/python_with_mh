from builtins import any
from builtins import all

from lesson import GLOBAL_NAMES

def _import_error(func_name):
	print(f"IMPORT ERROR: COULD NOT FIND FUNCTION {func_name!r} IN LESSON.PY")


def test_is_number_positive():
	try:
		from lesson import is_number_positive
	except ImportError:
		_import_error('is_number_positive')
		return False
	falses = [is_number_positive(x) for x in [-1, -2, -3, -4, -5]]
	trues = [is_number_positive(x) for x in [1, 2, 3, 4, 5]]
	return not any(falses) and all(trues) and is_number_positive(0) == "Neither"

def test_global_names():
	num_globals = len(GLOBAL_NAMES)
	set_globals = set(GLOBAL_NAMES)
	any_repeats = num_globals == len(set_globals)
	return any_repeats and set_globals == set(['var1', 'cool_func'])

def test_sort_chars():
	try:
		from lesson import sort_chars
	except ImportError:
		_import_error('sort_chars')
		return False
	args_and_expected = {'': '', 'a;lsidjf;asd': ';;aaddfijlss', '23l4km2l3k4234': '222333444kkllm', 'a': 'a'}
	return all([v == sort_chars(k) for k, v in args_and_expected.items()])

def test_dobby_search():
	try:
		from lesson import dobby_search
	except ImportError:
		_import_error('dobby_search')
		return False
	args_and_expected = {'': 'Dobby', 'abcdef': 'd', '23l4krm2l3k4234': '3', 'a': 'Dobby'}
	return all([dobby_search(k) for k, v in args_and_expected.items()])

def test_min_to_ord():
	try:
		from lesson import min_to_ord
	except ImportError:
		_import_error('min_to_ord')
		return False
	args_and_expected = {'': -1, '23l4km2l3k4234': 50, 'a': 97, 'thbjgk': 98}
	return all([v == min_to_ord(k) for k, v in args_and_expected.items()])

def test_max_to_ord():
	try:
		from lesson import max_to_ord
	except ImportError:
		_import_error('max_to_ord')
		return False
	args_and_expected = {'': -1, '23l4km2l3k4234': 109, 'a': 97, 'thbjgk': 116}
	return all([v == max_to_ord(k) for k, v in args_and_expected.items()])

def test_char_count():
	try:
		from lesson import char_count
	except ImportError:
		_import_error('char_count')
		return False
	args_and_expected = {('', 'x'): 0, ('23l4km2l3k4234', '2'): 3, ('a', 'a'): 1, ('thbjgk', 'a'): 0}
	return all([v == char_count(*k) for k, v in args_and_expected.items()])

def test_pretty_format():
	try:
		from lesson import pretty_format
	except ImportError:
		_import_error('pretty_format')
		return False
	args_and_expected = {'': 'No data found!', '       23l4km2l3k4234': '23l4km2l3k4234', 'a': 'a'}
	return all([v == pretty_format(k) for k, v in args_and_expected.items()])

if __name__ == "__main__":
    tests = [test_is_number_positive, test_global_names, test_sort_chars, test_dobby_search, test_min_to_ord, test_max_to_ord, test_char_count, test_pretty_format]
    for test in tests:
        test_value = test()
        if not test_value:
        	print(f"Test named {test.__name__!r} failed!")
    