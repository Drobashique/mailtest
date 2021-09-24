import pytest

def test_set_remove():
    a = set('012234')
    try:
        assert a.remove('5')
    except KeyError:
        pass
def test_set_union():
    a = set('012')
    b = set('1234')
    expected = set('01234')
    a = a.union(b)
    assert a==expected
    
def test_set_pop(fixture):
    a = set('0122121')
    b = a.pop()
    assert b in fixture
    
@pytest.fixture
def fixture():
    g = ['0','1','2']
    yield g

def test_dict_get():
    a = {'a': 1, 'b': 2, 'c':3}
    assert a.get('a')==1

def test_dict_clear():
    a = {'a': 1, 'b': 2, 'c':3}
    assert a.clear()== None

def test_dict_copy():
    a = {'a': 1, 'b': 2, 'c':3}
    b = a.copy()
    a['d'] = 4
    expected = {'a': 1, 'b': 2, 'c':3}
    assert b == expected
