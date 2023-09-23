from pathlib import Path
import os
from main import checkout
import logging
import pytest
import yaml

with (open('config.yaml') as f):
    data = yaml.safe_load(f)


@pytest.fixture()
def make_folders():
    return checkout(f"mkdir -p {data['folderin']} {data['folderout']} {data['folderext']}", '')


@pytest.fixture()
def make_files():
    return checkout(f"cd {data['folderin']} touch file1 file2", '')


@pytest.fixture()
def logger_var1():
    logging.basicConfig(level=logging.INFO, filename=f"{data['folderout']}stat.txt", filemode="a",
                        encoding="UTF-8", format="%(asctime)s %(levelname)s %(message)s")
    folder = Path('/home/alex/PycharmProjects/pythonProject/')
    count = 0
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.yaml'):
                count += 1
                logging.info(os.path.getsize(f'{folder}{file}'))
    logging.info(f"Count of configuration's files = {count}")
    with open('/proc/loadavg', 'r') as ff:
        proc_info = ff.read()
    logging.info(proc_info)
