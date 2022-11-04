import pytest 
from utils import dict_to_string 
from utils import get_query


class FakeRow:
    def __init__(self, d):
     
        self.d = d
    def _asdict(self):
        return self.d


class TestDictToString:
    def test_empty_dict(self):
        empty_dict = [FakeRow({})]
        got = dict_to_string(empty_dict)
        assert got == '\n'

    def test_single_dict(self):
        single_dict = [FakeRow({'a': 1,'b': 2})]
        got = dict_to_string(single_dict)
        assert got == 'a: 1;b: 2\n'


class TestGetQuery:
    def test_empty_script(self):
        empty_script = ''
        with pytest.raises(FileNotFoundError):
            get_query(empty_script)

    def test_wrong_request_type(self):
        wrong_request_type = 'not_sql_script.txt'
        with pytest.raises(FileNotFoundError):
            get_query(wrong_request_type)

    
     

