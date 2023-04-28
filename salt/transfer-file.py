import os
import sys
import subprocess

if len(sys.argv) != 2:
    print("Неверное количество аргументов")
    print("Пример: python transfer_file.py <clientID>")
    sys.exit(1)

clientID = sys.argv[1]
print("Начинаю перенос файлов для клиентов "+clientID)
process = subprocess.Popen(['sudo', 'salt', "*", 'state.apply', 'nginx_file_send'],
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
if stderr:
    print("Ошибка переноса файлов для клиентов "+clientID)
    print("Логи запишутся в файл /var/log/salt/transfer_file.log")
    with open("/var/log/salt/transfer_file.log", "w") as file:
        file.write(stderr.decode("utf-8"))
    print(stderr.decode("utf-8"))
    print(stdout.decode("utf-8"))
    sys.exit(1)
print("Перенос файлов для клиентов "+clientID+" завершен")
print(stdout.decode("utf-8"))
sys.exit(0)
