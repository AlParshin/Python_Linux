from main import checkout
from main import checkout_list_of_files
import pytest
import yaml

with (open('config.yaml') as f):
    data = yaml.safe_load(f)


def test_step1():
    assert checkout(f"cd {data['folderin']}; 7z a {data['folderout']}/arh1",
                    'Everything is Ok'), 'test_step1 FAIL'
    conftest.logger('test_step1')


def test_step2():
    assert checkout(f"cd {data['folderout']}; 7z d arh1.7z",
                    'Everything is OK'), 'test_step2 FAIL'


def test_step3():
    assert checkout(f"cd {data['folderext']}; 7z u {data['folderout']}/arh1",
                    'Everything is OK'), 'test_step3 FAIL'


def test_step4():
    assert checkout_list_of_files(
        f"cd {data['folderin']}; 7z l {data['folderout']}/arh1", 'Everything is OK'), 'test_step4 FAIL'


def test_step5():
    assert checkout(f"cd {data['folderin']}; 7z x {data['folderout']}/arh1",
                    'Everything is OK'), 'test_step5 FAIL'


if __name__ == '__main__':
    pytest.main(['-vv'])
