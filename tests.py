# ��������� ���������� ����������

import os
import shutil
import pytest

# ���������� ���������� �������� ��� ���� ����������

filePath = "/Users/�����/File_Manager/test.txt"  # ����
dirPath = "/Users/�����/File_Manager/test"  # �����
OS = "darwin"  # ������������ �������


# ������� ��������� ��������

# ������ ������� ���������������

@pytest.fixture
def wiam():
    if "File_Manager" not in dirPath:
        print("����� �� ������� ������� �����")
    else:
        print("/Users/�����/File_Manager/test")
        return True


# ������� �����

@pytest.fixture
def mkdr():
    if "File_Manager" not in dirPath:
        print("���������� ������� �����")
    else:
        os.mkdir(dirPath)
        return True


# ������� �����

@pytest.fixture
def dldr():
    if "File_Manager" not in dirPath:
        print("���������� ������� �����")
    else:
        os.rmdir(dirPath)
        return True


# ������� ����

@pytest.fixture
def mkfl():
    file = open(filePath, "w+")
    file.close()
    return True


# �������� � ����

@pytest.fixture
def wrtfl():
    try:
        line = "It's test line! :)"
        f = open(filePath, "a")
        f.write(line)
        f.close()
        return True
    except FileExistsError:
        print("file does not exist")


# �������� ���������� �����

@pytest.fixture
def shw():
    try:
        file = open(filePath, "r")
        print(file.read())
        file.close()
        return True
    except FileExistsError:
        print("file does not exists")

# ����������� ����

@pytest.fixture
def cpfl():
    try:
        fullNewPath = "/Users/�����/File_Manager/test_new.txt"
        shutil.copyfile(filePath, fullNewPath)
        return True
    except FileExistsError:
        print("file does not exist")


# ������������� ����

@pytest.fixture
def rnmfl():
    try:
        fullNewPath = "/Users/�����/File_Manager/test_.txt"
        os.rename(filePath, fullNewPath)
        return True
    except FileNotFoundError:
        print("file does not exist")


# ����������� ����

@pytest.fixture
def mvfl():
    try:
        fullNewPath = "/Users/�����/File_Manager/test_new.txt"
        fullNewPath2 = "/Users/�����/File_Manager/test_new_new.txt"
        shutil.copyfile(fullNewPath, fullNewPath2)
        os.remove(fullNewPath)
        return True
    except FileNotFoundError:
        print("file does not exist")


# ������� ����

@pytest.fixture
def dlfl():
    try:
        filePath = "/Users/�����/File_Manager/test_.txt"
        os.remove(filePath)
        return True
    except FileExistsError:
        print("file does not exist")

# �������� �����

def test_wiam(wiam):
    assert (wiam == True)


def test_mkdr(mkdr):
    assert (mkdr == True)


def test_mkfl(mkfl):
    assert (mkfl == True)


def test_wrtfl(wrtfl):
    assert (wrtfl == True)


def test_shw(shw):
    assert (shw == True)


def test_cpfl(cpfl):
    assert (cpfl == True)


def test_rnmfl(rnmfl):
    assert (rnmfl == True)


def test_mvfl(mvfl):
    assert (mvfl == True)


def test_dldr(dldr):
    assert (dldr == True)

def test_dlfl(dlfl):
    assert (dlfl == True)