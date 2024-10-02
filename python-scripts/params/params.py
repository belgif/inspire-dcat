import os
import pandas
import csv
import getpass
import traceback


# A cache for the get_param function. Keys are file paths and values are internal pandas objects to access
# the excel's content.
_excel_cache = {}


def get_param(key, path="params.xlsx", column=None):
    """
    :param key: a string to be found in the first column of the excel file.
    :param path: the path of the file containing the (key, value) definitions. If 'path' is relative, the stacktrace
    will be walked (bottom-up) until the combination of the script's directory and the relative path contains the
    specified key.
    :param column: the column name of the values (the second one if not specified).
    :return: a parameter matching a key stored in the first sheet of an excel file. The sheet must have a header.
    """
    if not os.path.isabs(path):
        for p, _, _, _ in traceback.extract_stack():
            p = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(p)), path))
            if not os.path.exists(p):
                continue
            if p not in _excel_cache:
                _excel_cache[p] = pandas.read_excel(p, index_col=0)
            if key in _excel_cache[p].index.values:
                path = p
                break

    if path not in _excel_cache:
        _excel_cache[path] = pandas.read_excel(path, index_col=0)

    return _excel_cache[path].at[key, column if column else _excel_cache[path].columns[0]]


def _get_pwd_helper(host, user, pwd_file):
    with open(pwd_file) as csvfile:
        c = csv.reader(csvfile, delimiter=',', quotechar='"')
        for h, u, pwd in c:
            if h == host and u == user:
                return pwd
    return None


def get_pwd(host, user, pwd_file='pwd.csv'):
    """
    :param host: a string, together with 'user', it will be used as a key to look for a password in the 'pwd_file'.
    :param user: a string, together with 'host', it will be used as a key to look for a password in the 'pwd_file'.
    :param pwd_file: the relative or obsolute path of the password file.
    :return: returns a password for the user 'user' on host 'host'. If no matching host and user is found in the file
    'pwd_file', the password must be interactively typed on the command prompt.
    """
    if not os.path.isabs(pwd_file):
        for p, _, _, _ in traceback.extract_stack():
            p = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(p)), pwd_file))
            if not os.path.exists(p):
                continue
            pwd = _get_pwd_helper(host, user, p)
            if pwd:
                return pwd
    else:
        pwd = _get_pwd_helper(host, user, pwd_file)
        if pwd:
            return pwd
    return getpass.getpass('password for user {0} on host {1}:'.format(user, host))
