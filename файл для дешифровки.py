import pyAesCrypt # для шифровки файлов
import os   # ходит по директориям и ищет файлы

# функция дешифровки файла
def decryption(file, password):

    # задаём рамер буфера
    buffer_size = 512 * 1024

    # вызываем метод расшифровки
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )

    # чтобы видеть результат вывожу на печать имя зашифрованного файла
    print("[Файл '" + str(os.path.splitext(file)[0]) + "' зашифрован]")
    # удаляю исходный файл с помощью функции remove
    os.remove(file)

# функция сканирования директорий
def walking_by_dirs(dir, password):

    # перебираю все поддиректории в указанной директории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # если находим файл, то дешифруем его
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        # если находим директории, то повторяем цикл в поисках файлов
        else:
            walking_by_dirs(path, password)

password = input("Введите пароль для шифрования: ")
walking_by_dirs("", password)
