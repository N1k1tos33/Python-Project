# Форензика — предназначена для "компьютерной криминалистики".
#Принцип работы программы будет следующий: если у нас получится
# открыть порт для приёма новых соединений, то значит он был открытым,
# если же нам выдаст ошибку, то это означает, что порт открыть нельзя,
# т.к. он занят уже каким-либо сервисом. Что за сервис? Загадка.
import socket # импортирую модуль для работы с соединением
import subprocess
from charset_normalizer.md import List
import psutil
import re
import os
import signal # модуль, в котором есть специальные константы,
# которые говорят о том, как надо себя вести осиротевшим процессам
import time

def check_is_port_opened(port: int) -> bool:
    '''Returns True if opened, False if closed'''

    opened = False  # переменная открытого порта устанавливается изначально в False
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', port))
        #sock.bind(('127.0.0.1', 8080)) пример
        #подключаем сокет по IP адресу нашего компьютера и порту

        sock.listen(5)
        sock.close()
    except socket.error as e:
        #print('Порт занят')
        # если возникла ошибка, то не меняем переменную, она остаётся в False
        pass
    else:
        # если код выполнился без ошибки, значит, мы смогли установить прослушку порта, а значит, он был открыт
        opened = True

    # возвращаем логическое значение
    return opened
#print(check_is_port_opened(8080))
#for i in range(1024, 65535):
    #print (f'Потр {i} открыт - {check_is_port_opened(i)}')
with open('ports.txt', 'at') as f:
    for i in range(1024, 65535):
        f.write(f'Port {i} is opened - {check_is_port_opened(i)}|n')

# пишем функцию, которая возвращает список словарей
# (from typing import List, если хотите )
def check_active_connections() -> List[dict]:
    """ Returns list of all listening connections """

# import subprocess не забываем, модуль идёт в комплекте, его не надо устанавливать
# через pip subprocess - это почти что то же самое, что написать какую-либо команду
# в консоль метод check_output() принимает список, где первый элемент - команда,
# а все последующие - параметры для команды, в нашем случае  -na мы получаем
# фактически то же самое, что вывелось бы нам на экран в консоли, и записываем
# это в переменную output
    output = subprocess.check_output(['netstat', '-na']).decode('cp866')

    # находим все пробелы, чтобы в дальнейшем распарсить нашу строку на словарь
    spaces = re.findall(r'\s+', output)
    strings = output.split('\n')

    # заменяем несколько пробелов в строке на один пробел, чтобы потом понимать, где именно лежит какой параметр
    for space in spaces:
        for i in range(len(strings)):
            strings[i] = strings[i].replace(space, ' ')

    listening = []

    print(len(strings))

    # в каждой строке теперь есть следующая инфа которую удобно распарсить
    # не забываем, что списки начинаются с 0!!!
    for string in strings:
        if string.find('LISTENING') > 0:
            splited = string.split(' ')
            listening.append(
                {
                    'type': splited[1],  # элемент 1 - это тип подключения
                    'adress': splited[3],  # элемент 3 - адрес, с которого установлено соединение
                    'status': splited[4].strip(),  # аргумент 4 - это состояние нашего подключения
                }
            )

    # возвращаем список словарей
    return listening


def get_running_proccesses() -> list:
    ''' Returns list of all running processes '''
    # получаем генератор для всех процессов
    processes_iter = psutil.process_iter()

    processes = []

    # добавляем объекты из генератора в список
    for process in processes_iter:
        processes.append(
            {
                'name': process.name(),
                'pid': process.pid,
                'memory used': process.memory_info().vms / 1024 ** 2,
# чтобы получить размер занимаемой памяти в мегабайтах,
# а не в байтах необходимо выполнить несколько математических действий
            }
        )

    processes = sorted(processes, key=lambda d: d['memory used'], reverse=True)
    # сортируем процессы по ключу в словарях "memory used"

    return processes  # возвращаем все процессы


# напишем функцию, которая убивает собственный процесс, т.е. суицидится иными словами
def suicide() -> None:
    self_pid = os.getpid()  # получаем айди запущенного программой процесса

    # для наглядности выведем сообщение перед тем, как процесс погибнет
    print('Before suicide')
    time.sleep(3)  # подождём три секунды, перед тем, как самоубиться
    os.kill(self_pid, signal.SIGBREAK)  # убиваемся в LINUX будет SIGSTOP

    print('After suicide :)')
# а вот это сообщение мы никогда не увидим, ведь программа к тому моменту уже будет мертва...

#print(get_running_proccesses())
suicide()