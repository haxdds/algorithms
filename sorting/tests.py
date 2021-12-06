import json
from selection_sort import selection_sort
f = open('./sorting/testing_data.json')

tests = json.load(f)

sorting_tests = tests['sorting_tests']


def test_selection_sort():
    
    for test in sorting_tests:
        a = test['input']
        assert selection_sort(a) == test['output']