#Принцип работы программы будет следующий: если у нас получится
# открыть порт для приёма новых соединений, то значит он был открытым,
# если же нам выдаст ошибку, то это означает, что порт открыть нельзя,
# т.к. он занят уже каким-либо сервисом. Что за сервис? Загадка.
import socket # импортируем нужный модуль
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