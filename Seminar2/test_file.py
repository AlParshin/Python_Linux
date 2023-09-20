from main import checkout
from main import checkout_list_of_files
import pytest

folderin = '/home/user/test'
folderout = '/home/user/out'
folderext = '/home/user/folder1'


def test_step1():
    assert checkout(f'cd {folderin}; 7z a {folderout}/arh1',
                    'Everything is OK'), 'test_step1 FAIL'


def test_step2():
    assert checkout(f'cd {folderout}; 7z d arh1.7z',
                    'Everything is OK'), 'test_step2 FAIL'


def test_step3():
    assert checkout(f'cd {folderext}; 7z u {folderout}/arh1',
                    'Everything is OK'), 'test_step3 FAIL'


def test_step4():
    assert checkout_list_of_files(
        f'cd {folderin}; 7z l {folderout}/arh1', 'Everything is OK'), 'test_step4 FAIL'


def test_step5():
    assert checkout(f'cd {folderin}; 7z x {folderout}/arh1',
                    'Everything is OK'), 'test_step5 FAIL'


if __name__ == '__main__':
    pytest.main(['-vv'])
