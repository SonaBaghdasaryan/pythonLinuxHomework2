# Установить пакет для расчёта crc32
# sudo apt install libarchive-zip-perl
# • Доработать проект, добавив тест команды расчёта хеша (h). Проверить, что хеш совпадает
# с рассчитанным командой crc32.


from check import checkout
from check import calc_crc32

out = "/home/user/out"


def test_1():
    assert (checkout("cd {};7z h arx2.7z".format(out), calc_crc32(None, 'hash_crc'))), "Test1 FAIL"