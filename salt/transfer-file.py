import os
import sys
import subprocess

if len(sys.argv) != 2:
    print("Неверное количество аргументов")
    print("Пример: python transfer_file.py <clientID>")
    sys.exit(1)

clientID = sys.argv[1]
print("Начинаю перенос файлов для клиента "+clientID)
process = subprocess.Popen(['sudo', 'salt', clientID, 'state.apply', 'nginx_files_send'],
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
out = stdout.decode("utf-8")
if stderr:
    print("Ошибка переноса файлов для клиентов "+clientID)
    err = stderr.decode("utf-8")
    print("Логи запишутся в файл /var/log/salt/transfer_file.log")
    with open("/var/log/salt/transfer_file.log", "w") as file:
        file.write(err)
    print(err)
    sys.exit(1)
print("Перенос файлов для клиентов "+clientID+" завершен")
sys.exit(0)
