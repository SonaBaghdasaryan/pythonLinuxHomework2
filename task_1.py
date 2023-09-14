# Дополнить проект тестами, проверяющими команды вывода списка файлов (l) и разархивирования с путями (x).

from check import checkout

out = "/home/user/out"


def test_1():
    res1 = checkout("cd {};7z x arx2.7z".format(out), "Everything is Ok")
    res2 = checkout("ls {}".format(out), "test1")
    assert res1 and res2, "test1 FAIL"

def test_2():
    assert (checkout("cd {};7z l arx2.7z".format(out), "test2")), "test2 FAIL"
