import subprocess


def checkout(cmd, text):
    result = subprocess.run(
        cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')

    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def checkout_list_of_files(cmd, text):
    result = subprocess.run(
        cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')

    if 'file1.txt' in result.stdout and 'file2.txt' in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def checkout_negative(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE,
                            encoding='utf-8', stderr=subprocess.PIPE)

    if text in result.stdout or text in result.stderr:
        return True
    else:
        return False
